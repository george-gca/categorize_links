_RESEARCH_URLS = (
    'aclanthology.',
    'acm.',
    '.ai/',
    'allenai.',
    'analyticsindiamag.',
    'arxiv.',
    'facebookresearch.',
    '.google',
    'huggingface.',
    'ieeexplore.',
    'marktechpost.',
    'meta.',
    'mit.',
    'nature.',
    'neurosciencenews.',
    'nips.',
    'openaccess.',
    'openreview.',
    'papers.',
    'paperswithcode.',
    'proceedings.',
    'research.',
    'sciencedirect.',
    'scitechdaily.',
    'springer.',
    'stanford.',
    'towardsdatascience.',
)


def remove_duplicates(links: list[str]) -> list[str]:
    # remove duplicates keeping the order
    seen = set()
    return [link for link in links if not (link in seen or seen.add(link))]


def categorize_links(links: str) -> tuple[list[str], list[str]]:
    research_links = []
    other_links = []

    for line in links.split('\n'):
        link = line.replace('"', '').strip()
        if len(link) > 0 and link != 'chrome-native://newtab/':
            if any(research_url in link for research_url in _RESEARCH_URLS):
                research_links.append(link)
            else:
                other_links.append(link)

    return research_links, other_links
