import country
import tourist

touristCenters = [
    tourist.TouristCenters(1, "Umuahia", "One local place like that"),
    tourist.TouristCenters(2, "Aba", "One super local place like that"),
    tourist.TouristCenters(3, "Owerri", "One flexi place like that"),
    tourist.TouristCenters(4, "Lagos", "One place like that"),
    tourist.TouristCenters(5, "Abuja", "One great place like that"),
]

coutries = [
    country.Country(1, "Nigeria", touristCenters),
    country.Country(1, "Rwanda", touristCenters),
    country.Country(1, "Cameroon", touristCenters),
    country.Country(1, "Ghana", touristCenters),
    country.Country(1, "Canada", touristCenters),
    country.Country(1, "South Africa", touristCenters),
]


print("Welcome to the Tourist Center App")
print("Here are the countries we have:")


def startApp():

    for country in coutries:
        print(country.name)

    userCountryInput = input("Select a country: ")

    selectedCountry = next(
        (country for country in coutries if country.name == userCountryInput), None
    )

    if selectedCountry is not None:
        print("Tourist centers in " + selectedCountry.name)
        print("")

        for touristCenter in selectedCountry.touristCenters:
            print(touristCenter.name)

        userTouristCenterInput = input("Select a tourist center: ")
        selectedTouristCenter = next(
            (tourist for tourist in selectedCountry.touristCenters if tourist.name ==
             userTouristCenterInput), None
        )

        if selectedTouristCenter is not None:
            print("More information about this center: " +
                  selectedTouristCenter.info)
    else:
        print("Country not found")
        startApp()


startApp()
