from Dropdowns.dropdowns import Dropdowns

with Dropdowns() as bot:
    #Affiliate Dropdown
    bot.land_first_page()
    bot.dropdown_affiliate()
    bot.go_to_learn()
    bot.click_back_btn()
    bot.dropdown_affiliate()
    bot.go_to_getting_started()
    bot.click_back_btn()
    bot.dropdown_affiliate()
    bot.go_to_how_to_make_money()
    bot.click_back_btn()
    bot.dropdown_affiliate()

    #Event Dropdown
    bot.dropdown_event()
    bot.go_to_influencer_marketing()
    bot.click_back_btn()
    bot.dropdown_event()
    bot.go_to_networks()
    bot.click_back_btn()

    #About Us Dropdown
    bot.dropdown_about_us()
    bot.go_to_case_studies()
    bot.click_back_btn()
    bot.dropdown_about_us()
    bot.go_to_who_we_are()
    bot.click_back_btn()

    #Support Dropdown
    bot.dropdown_support()
    bot.go_to_affiliate_support()
    bot.click_back_btn()
    bot.dropdown_support()
    bot.go_to_customer_services_support()
    bot.click_back_btn()
    bot.dropdown_support()
    bot.go_to_vendor_support()
    bot.click_back_btn()

    #Blog Page
    bot.go_to_blog()
    bot.click_back_btn()
