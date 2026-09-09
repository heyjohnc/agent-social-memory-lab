"""Export allowlisted experiment metrics without identities, messages or credentials."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path


def read(path, fallback):
    return json.loads(path.read_text()) if path.exists() else fallback


def lines(path):
    if path.exists():
        with path.open() as handle:
            for line in handle:
                try:
                    yield json.loads(line)
                except ValueError:
                    continue


def collect(workspace):
    peers = read(workspace / 'social_friends.json', {})
    config = read(workspace / 'agent_config.json', {})
    home = read(workspace / 'run_status.json', {})
    outside = read(workspace / 'excursion_status.json', {})
    learning = read(workspace / 'social_learning_status.json', {})
    visits = list(lines(workspace / 'excursions.jsonl'))
    events = list(lines(workspace / 'social_events.jsonl'))
    invitations = [r for r in visits if 'https://technocore.chat/humans#r/technosex' in r.get('receipt', {}).get('text', '')]
    guests = {e['peer'] for e in events if e.get('kind') == 'guest_observed'}
    invited = {(r.get('target_message') or {}).get('from') for r in invitations}
    return {
        'captured_at_utc': datetime.now(timezone.utc).isoformat(),
        'counts': {
            'home_posts': sum(home.get('sent', {}).values()),
            'external_posts': len(visits),
            'confirmed_peer_identities': sum(p.get('explicit_replies', 0) > 0 for p in peers.values()),
            'explicit_references': sum(p.get('explicit_replies', 0) for p in peers.values()),
            'invitations': len(invitations),
            'guest_identities_since_pilot': len(guests),
            'guest_answers_since_pilot': sum(e.get('kind') == 'guest_answered' for e in events),
            'guests_also_invited': len(guests & invited),
        },
        'configuration': {
            'home_interval_seconds': config.get('reaction_seconds'),
            'models': {role: data.get('model') for role, data in config.get('roles', {}).items()},
            'deadline_utc': datetime.fromtimestamp(home['deadline'], timezone.utc).isoformat() if home.get('deadline') else None,
        },
        'status': {
            'home': home.get('status'), 'outside': outside.get('status'),
            'reflection_last_success_utc': datetime.fromtimestamp(learning['last_success'], timezone.utc).isoformat() if learning.get('last_success') else None,
            'reflection_has_error': learning.get('last_error') is not None,
        },
        'limitations': 'Mixed counting windows; incomplete observations; identities are not independent users. No causal conversion or learning claim.',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workspace', type=Path, required=True)
    args = parser.parse_args()
    data = collect(args.workspace)
    destination = Path(__file__).resolve().parents[1] / 'experiments'
    destination.mkdir(exist_ok=True)
    path = destination / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(path)


if __name__ == '__main__':
    main()
