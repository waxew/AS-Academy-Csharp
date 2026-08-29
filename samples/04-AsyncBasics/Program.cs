// نمونه آموزشی async/await و CancellationToken.
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(5));

try
{
    string result = await SimulateIoAsync(cts.Token);
    Console.WriteLine(result);
}
catch (OperationCanceledException)
{
    Console.WriteLine("Operation cancelled.");
}

static async Task<string> SimulateIoAsync(CancellationToken cancellationToken)
{
    await Task.Delay(500, cancellationToken);
    return "Async operation completed.";
}
