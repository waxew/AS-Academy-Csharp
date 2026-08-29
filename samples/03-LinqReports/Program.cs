// نمونه آموزشی LINQ: فیلتر، گروه‌بندی و projection.
var products = new[]
{
    new Product("Keyboard", "Hardware", 1200m, true),
    new Product("Mouse", "Hardware", 500m, true),
    new Product("Course", "Education", 900m, true),
    new Product("Legacy", "Education", 100m, false)
};

var report = products
    .Where(product => product.IsActive)
    .GroupBy(product => product.Category)
    .Select(group => new
    {
        Category = group.Key,
        Count = group.Count(),
        Total = group.Sum(product => product.Price)
    });

foreach (var row in report)
{
    Console.WriteLine($"{row.Category}: {row.Count} / {row.Total:N0}");
}

public sealed record Product(string Name, string Category, decimal Price, bool IsActive);
