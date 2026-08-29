// مینی‌پروژه آموزشی: جمع هزینه‌ها با مدل immutable-style ساده.
var expenses = new List<Expense>
{
    new("Coffee", 120_000m),
    new("Book", 450_000m),
    new("Internet", 300_000m)
};

// LINQ برای محاسبه مجموع هزینه‌ها استفاده می‌شود.
decimal total = expenses.Sum(item => item.Amount);
Console.WriteLine($"Total: {total:N0}");

// record برای مدل داده کوچک و value-oriented مناسب است.
public sealed record Expense(string Title, decimal Amount);
