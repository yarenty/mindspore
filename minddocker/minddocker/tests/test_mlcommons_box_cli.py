from click.testing import CliRunner
from minddocker.main import cli

runner = CliRunner()

def test_md():
    response = runner.invoke(cli)
    assert response.exit_code == 0
    print(response.output)
    assert 'Usage: md [OPTIONS] COMMAND [ARGS]...' in response.output
    assert 'mind-docker 📦 is a packaging tool for ML models' in response.output
    assert 'verify  Verify MD metadata' in response.output
