from django.shortcuts import render

def show_main(request):
    context = {
        'tagline': "Your Daily Dose of Sweetness",
        'description': "Welcome to Butter & Batter — where every bite is a blissful journey of flavors.",
        'food_items': [
            {
                'name': 'Classic Croissant',
                'price': "Rp25.000",
                'description': "Flaky, buttery, and oh-so-delicious. Our classic croissant is made with layers of love and pure butter for that perfect golden crisp and a melt-in-your-mouth experience."
            },
            {
                'name': 'Velvet Cupcakes',
                'price': "Rp30.000",
                'description': "Soft, moist, and velvety smooth, topped with our signature cream cheese frosting. These cupcakes are more than just a treat; they are a celebration in every bite."
            },
            {
                'name': 'Lemon Drizzle Loaf',
                'price': "Rp25.000",
                'description': "Bright and zesty, with a burst of lemon in every slice, our Lemon Drizzle Loaf is the perfect balance of sweet and tangy. Ideal for sunny afternoons and teatime delights."
            },
            {
                'name': 'Artisan Sourdough Bread',
                'price': "Rp20.000",
                'description': "Crafted with patience and care, our sourdough bread is naturally fermented for that perfect tangy taste and a satisfying chewy texture. Baked fresh every morning!"
            },
        ]
    }

    return render(request, 'main.html', context)
