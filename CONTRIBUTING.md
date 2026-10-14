# Contributing

Thanks for helping build a useful, accurate catalog.

## Add an entry

Create one JSON file under data/apps/ and follow the schema in data/schema/app.schema.json.

Use status: existing for a public project that can be inspected today. Use status: planned for a build proposal that does not have a repository yet. Planned entries must use repoUrl: null and openSourceStatus: planned.

Every entry should:

- Describe a concrete user workflow rather than a vague product category.
- Name comparable paid workflows without claiming feature parity.
- Include limitations and meaningful dependencies.
- Link to a source-directory record when the idea came from another catalog.
- Use openSourceStatus: open-source only when a recognizable license is visible.
- Mark vibe-coded evidence as unverified unless the author or maintainer has documented it.

Run the validator before submitting:

~~~bash
python scripts/validate.py
~~~

## Evidence

Use one of these evidence labels:

- author-claimed — the author describes the project as AI-assisted or vibe-coded.
- maintainer-verified — a maintainer has verified the development claim.
- unverified — the project is a useful candidate, but the development process is not documented.

The label describes evidence about the development process. It does not describe code quality.

## Safety and accuracy

- Never commit API keys, tokens, private URLs, or personal data.
- Prefer official APIs and OAuth flows.
- Do not recommend bypassing access controls, paywalls, or rate limits.
- Do not copy licensed datasets or proprietary product content.
- Keep alternative claims bounded and factual.
- Update lastVerified when checking a project's status, license, or links.

## Pull request checklist

- [ ] The entry validates locally.
- [ ] The slug matches the filename.
- [ ] URLs are public and correct.
- [ ] License status is accurate.
- [ ] Limitations and dependencies are documented.
- [ ] No secrets or private information are included.

## License

By contributing, you agree that your contribution is provided under the MIT License.
