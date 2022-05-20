class SkiplaggedLocators():

### locators for home page
    # top row links
    SKIPLAGGED_TR_SKIPLAGGED_LINK = '//div[@class="header-left"]//span[@class="hide-small"]'
    SKIPLAGGED_TR_FLIGHTS_LINK = '//div[@class="header-left"]//a[@href="/flights"]'
    SKIPLAGGED_TR_HOTELS_LINK = '//div[@class="header-left"]//a[@href="/hotels"]'
    SKIPLAGGED_TR_CARS_LINK = '//div[@class="header-left"]//a[text()="Cars"]'
    SKIPLAGGED_TR_REWARDS_LINK = '//div[@class="header-left"]//a[text()="Rewards"]'
    SKIPLAGGED_TR_LOGIN_LINK = '//a[text()="Login"]'

    SKIPLAGGED_HOME_HEADER = '//div[@class="flight-search"]//h1'
    SKIPLAGGED_DEPARTURE_AIRPORT_INPUT = '//input[contains(@class,"src-input")]'
    SKIPLAGGED_DESTINATION_AIRPORT_INPUT = '//input[contains(@class,"dst-input")]'
    SKIPLAGGED_DEPART_DATE_INPUT = '//input[@placeholder="Depart"]'
    SKIPLAGGED_RETURN_DATE_INPUT = '//input[@placeholder="Return"]'
    SKIPLAGGED_SEARCH_FLIGHTS_BUTTON = '//button[@type="submit"][text()="Search Flights"]'
    SKIPLAGGED_SEARCH_DEALS_BUTTON = '//button[@type="submit"][text()="Search Deals"]'

    SKIPLAGGED_ROUND_TRIP_OR_ONE_WAY_DROP_DOWN = '//div[@class="skip-select passengers-input-container trip-type-select"]//button'
    SKIPLAGGED_ROUND_TRIP_OR_ONE_WAY_DROP_DOWN_MENU_OPTIONS= '//div[@data-trip-type][text()="%s"]'

    SKIPLAGGED_TRAVELERS_OPTION = '//div[@class="skip-select passengers-input-container"]//button'
    SKIPLAGGED_TOTAL_NUMBER_OF_TRAVLERS = '//div[@class="skip-select passengers-input-container"]//button/span[text()="%s Travelers"]'
    SKIPLAGGED_ADULTS_TRAVELLERS = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]/span[text()="Adults"]/..'
    SKIPLAGGED_ADULTS_PLUS = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Adults")]/following-sibling::span/button[@data-delta="+1"]'
    SKIPLAGGED_ADULTS_MINUS = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Adults")]/following-sibling::span/button[@data-delta="-1"]'
    SKIPLAGGED_ADULTS_COUNT = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Adults")]/following-sibling::span/span'
    SKIPLAGGED_CHILDREN_TRAVELLERS = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Children")]/..'
    SKIPLAGGED_CHILDREN_PLUS = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Children")]/following-sibling::span/button[@data-delta="+1"]'
    SKIPLAGGED_CHILDREN_MINUS = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Children")]/following-sibling::span/button[@data-delta="-1"]'
    SKIPLAGGED_CHILDREN_COUNT = '//div[@class="skip-select passengers-input-container"]//div[@class="passengers-input__select-row"]//span[contains(text(), "Children")]/following-sibling::span/span'

    SKIPLAGGED_DEPART_OR_RETURN_DATE_SELECTED = '//div[@class="ui-datepicker-arrow"][@style]'
    SKIPLAGGED_CALENDAR_1_GROUP = '//div[@class="ui-datepicker-group ui-datepicker-group-first"]'
    SKIPLAGGED_CALENDAR_1_MONTH_NAME = '//div[@class="ui-datepicker-group ui-datepicker-group-first"]//span[@class="ui-datepicker-month"]'
    SKIPLAGGED_CALENDAR_1_DATES = '//div[@class="ui-datepicker-group ui-datepicker-group-first"]//a[@class="ui-state-default"][text()="%s"]'
    SKIPLAGGED_CALENDAR_2_GROUP = '//div[@class="ui-datepicker-group ui-datepicker-group-last"]'
    SKIPLAGGED_CALENDAR_2_MONTH_NAME = '//div[@class="ui-datepicker-group ui-datepicker-group-last"]//span[@class="ui-datepicker-month"]'
    SKIPLAGGED_CALENDAR_2_DATES = '//div[@class="ui-datepicker-group ui-datepicker-group-last"]//a[@class="ui-state-default"][text()="%s"]'
    SKIPLAGGED_CALENDAR_HIDDEN = '//div[@id="ui-datepicker-div"][contains(@style, "display: none")]'
    SKIPLAGGED_CALENDAR_NEXT_BUTTON = '//span[@class="ui-icon ui-icon-circle-triangle-e"][text()="Next"]'

    SKIPLAGGED_FEATURED_IN = '//div[@class="press-banner hide-small"]'
    SKIPLAGGED_REWARDS_AD = '//a[@href="/rewards/summary"][@class="affiliate-banner"]'

    SKIPLAGGED_HOME_PAGE_DEALS_HEADER_1 = '//div[@class="skip-deals"]/h1[text()="Find flights the airlines don’t want you to see."]'
    SKIPLAGGED_HOME_PAGE_DEALS_HEADER_2 = '//div[@class="skip-deals"]/h1//span'
    SKIPLAGGED_HOME_PAGE_DEALS_HEADER_3 = '//div[text()="Take a look"]'
    SKIPLAGGED_DEALS_CARDS = '//li[@class="deal"]'
    SKIPLAGGED_DEALS_LOCATION_INPUT = '//form[@class="explore-deals hide-small"]//input[@placeholder="Enter Location"]'
    SKIPLAGGED_DEALS_LOCATION_AUTOCOMPLETE = '//li[@class="ui-menu-item"]//span[@class="autocomplete-em"]'
    SKIPLAGGED_DEALS_LOCATION_TEXT = '(//li[@class="ui-menu-item"]/a)[1]'
    SKIPLAGGED_SEARCH_DEALS_BUTTON = '//form[@class="explore-deals hide-small"]//button[@type="submit"]'

    # footer locaters
    SKIPLAGGED_FOOTER_LOGO = '//div[@class="footer-logo"][text()="skiplagged"]'
    SKIPLAGGED_FOOTER_ABOUT = '//div[@class="footer-nav"]//a[@title="About"][text()="About"]'
    SKIPLAGGED_FOOTER_FAQ = '//div[@class="footer-nav"]//a[@title="FAQ"][text()="FAQ"]'
    SKIPLAGGED_FOOTER_PRESS = '//div[@class="footer-nav"]//a[@title="Press"][text()="Press"]'
    SKIPLAGGED_FOOTER_TERMS = '//div[@class="footer-nav"]//a[@title="Terms"][text()="Terms"]'
    SKIPLAGGED_FOOTER_CAREERS = '//div[@class="footer-nav"]//a[@title="Careers"][text()="Careers"]'
    SKIPLAGGED_FOOTER_LANGUAGE = '//div[@class="language-select"]//a[@class="dropdown-toggle"]'
    SKIPLAGGED_FOOTER_LANGUAGE_DROPDOWN = '//div[@class="language-select"]//ul[@class="dropdown-menu dropdown-menu-right"]'
    SKIPLAGGED_FOOTER_CURRENCY = '//div[@class="footer__dropdown-group"]//div[@class="currency-select"]//a[@class="dropdown-toggle"]'
    SKIPLAGGED_FOOTER_CURRENCY_DROPDOWN = '//div[@class="footer__dropdown-group"]//div[@class="currency-select"]//ul[@class="dropdown-menu dropdown-menu-right"]'
    SKIPLAGGED_FOOTER_FACEBOOK = '//div[@class="social-media-links"]//a[@data-alt="Facebook"]'
    SKIPLAGGED_FOOTER_TWITTER = '//div[@class="social-media-links"]//a[@data-alt="Twitter"]'
    SKIPLAGGED_FOOTER_INSTAGRAM = '//div[@class="social-media-links"]//a[@data-alt="Instagram"]'

#### locators for cheapest city flights when destination is Anywhere
    SKIPLAGGED_CHEAPEST_CITIES_CARD = '//div[@id="trip-list-skipsy"]//li'
    SKIPLAGGED_INDEX_CHEAPEST_CITIES_CARD_INDEX = '(//div[@id="trip-list-skipsy"]//li)[%s]'
    SKIPLAGGED_CHEAPEST_CITY = '//div[@id="trip-list-skipsy"]//li//h2[@class="skipsy-city"]'
    SKIPLAGGED_CHEAPEST_COUNTRY = '//div[@id="trip-list-skipsy"]//li//h2[@class="skipsy-city"]//span[@class="skipsy-region"]'
    SKIPLAGGED_CHEAPEST_PRICE = '//div[@id="trip-list-skipsy"]//li//div[@class="skipsy-cost"]'
    SKIPLAGGED_SKIPLAGGED_RATE = '//div[@id="trip-list-skipsy"]//li//div[@class="skipsy-cost skipsy-cost-hidden"]'

### locators after selecting a city
    SKIPLAGGED_PRICE_FILTER = '//div[@class="trip-list"][not(@style="display: none;")]//button[@data-sort="cost"]'
    SKIPLAGGED_DURATION_FILTER = '//div[@class="trip-list"][not(@style="display: none;")]//button[@data-sort="duration"]'
    SKIPLAGGED_LIST_OF_FLIGHTS = '//div[@class="infinite-trip-list"]'
    SKIPLAGGED_LIST_OF_FLIGHT_ROW = '//div[@class="infinite-trip-list"]/div/div[@id]'
    SKIPLAGGED_LIST_OF_FLIGHT_ROW_INDEX = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]'
    SKIPLAGGED_LIST_OF_FLIGHT_ROW_INDEX_FIRST_AIRPORT_TIME = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]'
    SKIPLAGGED_LIST_OF_FLIGHT_ROW_INDEX_LAST_AIRPORT = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]'
    SKIPLAGGED_TO_AIRPORT = '//input[contains(@class, "dst-input")]'
    SKIPLAGGED_FLIGHT_DURATION_INDEX = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//span[@data-translate]'
    SKIPLAGGED_FLIGHT_PRICE_ATTRIBUTE_INDEX = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//p[@data-orig-price]'
    SKIPLAGGED_FLIGHT_NUMBER_OF_STOP_INDEX = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//span[@class="trip-stops"]'

#### index locators of departure flight info
    SKIPLAGGED_INDEX_FLIGHT = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]'
    SKIPLAGGED_INDEX_FLIGHT_FIRST_DEPART_TAKEOFF = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-first"]/div[@class="trip-path-point-time "]'
    SKIPLAGGED_INDEX_FLIGHT_FIRST_AIRPORT = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-first"]//span[@class="airport-code"]'
    SKIPLAGGED_INDEX_FLIGHT_FIRST_CITY = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-first"]//span[@class="airport-city"]'
    SKIPLAGGED_INDEX_FLIGHT_FIRST_DURATION = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-spacer"][1]/div[@class="trip-path-spacer-label"]'
    SKIPLAGGED_INDEX_FLIGHT_LAST_ARRIVAL = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[contains(@class,"trip-path-point trip-path-point-last")][not(contains(@class, "skip"))]/div[contains(@class,"trip-path-point-time ")]'
    SKIPLAGGED_INDEX_FLIGHT_LAST_AIRPORT = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[contains(@class,"trip-path-point trip-path-point-last")][not(contains(@class, "skip"))]//span[@class="airport-code"]'
    SKIPLAGGED_INDEX_FLIGHT_LAST_CITY = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[contains(@class,"trip-path-point trip-path-point-last")][not(contains(@class, "skip"))]//span[@class="airport-city"]'
    SKIPLAGGED_INDEX_FLIGHT_LAYOVER_ARRIVAL = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-airport-demp same-layover"]/div[contains(@class, "trip-path-point-time ")]'
    SKIPLAGGED_INDEX_FLIGHT_LAYOVER_AIRPORT = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-airport-demp same-layover"]//span[@class="airport-code"]'
    SKIPLAGGED_INDEX_FLIGHT_LAYOVER_CITY = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-airport-demp same-layover"]//span[@class="airport-city"]'
    SKIPLAGGED_INDEX_FLIGHT_LAYOVER_DURATION = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-spacer layover same-layover"]/div[@class="trip-path-spacer-label"]'
    SKIPLAGGED_INDEX_FLIGHT_LAYOVER_DEPART_TAKEOFF = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point trip-path-point-airport-demp"]/div[contains(@class, "trip-path-point-time ")]'

    SKIPLAGGED_INDEX_FLIGHT_SKIP_LAYOVER_DURATION = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-spacer leg-skip layover same-layover"]/div[@class="trip-path-spacer-label"]'
    SKIPLAGGED_INDEX_FLIGHT_SKIP_LAYOVER_DEPART_TAKEOFF = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point leg-skip trip-path-point-airport-demp"]/div[contains(@class, "trip-path-point-time ")][contains(@data-original-title, "Depart")]'
    SKIPLAGGED_INDEX_FLIGHT_SKIP_LAYOVER_FLIGHT_DURATION = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-spacer leg-skip"]/div[@class="trip-path-spacer-label"]'
    SKIPLAGGED_INDEX_FLIGHT_SKIP_ARRIVAL = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point leg-skip trip-path-point-airport-demp"]/div[contains(@class, "trip-path-point-time ")][contains(@data-original-title, "Arriv")]'
    SKIPLAGGED_INDEX_FLIGHT_SKIP_ARRIVAL_AIRPORT = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point leg-skip trip-path-point-airport-demp"]/div[contains(@class, "trip-path-point-time ")][contains(@data-original-title, "Arriv")]/following-sibling::div//span[@class="airport-code"]'
    SKIPLAGGED_INDEX_FLIGHT_SKIP_ARRIVAL_CITY = '(//div[@class="infinite-trip-list"]/div/div[@id])[%s]//div[@class="trip-path-point leg-skip trip-path-point-airport-demp"]/div[contains(@class, "trip-path-point-time ")][contains(@data-original-title, "Arriv")]/following-sibling::div//span[@class="airport-city"]'
#### make xpaths that aren't as robust
#### we will need to test for flights that are and arent skiplagged
#### if they are skiplagged, we'll have to test to make sure there are other flights afterwards
#### and crossed out flights will have a different xpath

#### locators for flight filters
    SKIPLAGGED_FLIGHT_TYPE_HIDDEN = '//label[@class="filter-checkbox"]//input[@data-name="hiddenCity"]/following-sibling::span[text()="Hidden-City"]'
    SKIPLAGGED_FLIGHT_TYPE_HIDDEN_ONLY = '//label[@class="filter-checkbox"]//input[@data-name="hiddenCity"]/following-sibling::span[text()="only"]'
    SKIPLAGGED_FLIGHT_TYPE_STANDARD = '//label[@class="filter-checkbox"]//input[@data-name="standard"]/following-sibling::span[text()="Standard"]'
    SKIPLAGGED_FLIGHT_TYPE_STANDARD_ONLY = '//label[@class="filter-checkbox"]//input[@data-name="standard"]/following-sibling::span[text()="only"]'