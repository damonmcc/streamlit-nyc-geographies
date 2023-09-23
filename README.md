# NYC Geographies

...

## Development

### Local

1. Open the repo in VS Code using the defined dev container.
2. Make and save changes
3. Run the app locally with `streamlit run Home.py`
4. Open the app in any browser using the URL [localhost:8501](http://localhost:8501/)

### Deployment

This repo deploys the app using webhooks and two branches:

- `main`` -> [nyc-geographies.streamlit.app](https://nyc-geographies.streamlit.app/)
- `dev`` -> [nyc-geographies-dev.streamlit.app](https://nyc-geographies-dev.streamlit.app/)

On a push to either of those branches the relevant site is updated to reflect changes.

To reflect changes to python packages, an app must be rebuilt using the `Reboot` action in streamlit's app management UI.
