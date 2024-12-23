from flask import Flask, request, jsonify

# Define categories and corresponding disposal recommendations
disposal_methods = {
    "aerosol_cans": {"recommendation": "Make sure the can is empty before disposal. Check with your local recycling program for acceptance. If not recyclable, dispose of as hazardous waste.", "type": "recyclable"},
    "aluminum_food_cans": {"recommendation": "Rinse the can thoroughly to remove any food residue. Place it in your recycling bin. Crushing the can saves space but is optional.", "type": "recyclable"},
    "aluminum_soda_cans": {"recommendation": "Rinse to remove sticky residue. Place the can in your recycling bin. Avoid crushing if your recycling program requires intact cans.", "type": "recyclable"},
    "cardboard_boxes": {"recommendation": "Flatten the box to save space before recycling. Remove any non-cardboard elements like tape or labels. Place in the recycling bin for paper/cardboard.", "type": "recyclable"},
    "cardboard_packaging": {"recommendation": "Ensure all packaging is flattened for easy recycling. Remove non-cardboard parts such as plastic film or foam. Recycle with other cardboard materials.", "type": "recyclable"},
    "clothing": {"recommendation": "If still wearable, consider donating to local charities or thrift stores. For damaged clothing, recycle as fabric or take to textile recycling bins. Avoid placing in general waste.", "type": "recyclable"},
    "coffee_grounds": {"recommendation": "Coffee grounds are rich in nutrients and can be composted. Add them to your compost bin or garden soil. If composting is not an option, dispose of them in organic waste bins.", "type": "organic"},
    "disposable_plastic_cutlery": {"recommendation": "Most disposable cutlery is not recyclable. Place it in the general waste bin. Consider switching to reusable or compostable alternatives in the future.", "type": "non-recyclable"},
    "eggshells": {"recommendation": "Eggshells can be composted and are great for enriching soil. Add them to your compost bin after rinsing. Alternatively, place in organic waste bins.", "type": "organic"},
    "food_waste": {"recommendation": "Separate food waste from packaging before disposal. Compost if possible to reduce landfill impact. Use organic waste bins where available.", "type": "organic"},
    "glass_beverage_bottles": {"recommendation": "Rinse thoroughly to remove any liquid. Place in the glass recycling bin. Remove caps or lids if not made of glass.", "type": "recyclable"},
    "glass_cosmetic_containers": {"recommendation": "Clean the container to ensure it's residue-free. Recycle if your local program accepts glass containers. Broken glass should be wrapped in paper or cardboard and placed in general waste.", "type": "recyclable"},
    "glass_food_jars": {"recommendation": "Rinse the jar to remove food residue. Recycle in glass bins. Lids made of metal can often be recycled separately.", "type": "recyclable"},
    "magazines": {"recommendation": "Remove plastic covers or non-paper elements before recycling. Place in your paper recycling bin. Avoid recycling if excessively wet or damaged.", "type": "recyclable"},
    "newspaper": {"recommendation": "Keep newspapers dry and free of contaminants like food stains. Recycle them in designated paper bins. Bundle them for easier handling if required.", "type": "recyclable"},
    "office_paper": {"recommendation": "Shred confidential documents if necessary before recycling. Avoid including paper with heavy lamination or plastic content. Recycle in paper bins.", "type": "recyclable"},
    "paper_cups": {"recommendation": "Check for a recycling symbol to confirm if recyclable. Most paper cups with plastic lining are not recyclable and go into general waste. Consider switching to reusable cups.", "type": "non-recyclable"},
    "plastic_cup_lids": {"recommendation": "If marked recyclable, clean and place them in the appropriate bin. Otherwise, dispose of in general waste. Avoid using single-use lids when possible.", "type": "non-recyclable"},
    "plastic_detergent_bottles": {"recommendation": "Rinse out any remaining detergent to avoid contamination. Check the recycling symbol and place in plastics recycling. Keep the lid on if acceptable.", "type": "recyclable"},
    "plastic_food_containers": {"recommendation": "Ensure the container is clean and free of food residue. Recycle if marked as recyclable. Otherwise, dispose of in general waste.", "type": "recyclable"},
    "plastic_shopping_bags": {"recommendation": "Reuse them for storage or garbage liners. If recycling facilities for plastic bags are available, drop them off. Avoid throwing in general recycling bins.", "type": "non-recyclable"},
    "plastic_soda_bottles": {"recommendation": "Empty and rinse the bottle before recycling. Leave the cap on if your recycling program accepts it. Crush the bottle to save space if desired.", "type": "recyclable"},
    "plastic_straws": {"recommendation": "Plastic straws are not recyclable in most programs. Dispose of them in general waste. Consider using reusable or biodegradable straws.", "type": "non-recyclable"},
    "plastic_trash_bags": {"recommendation": "Trash bags themselves are not recyclable. Dispose of them in general waste along with their contents. Look for biodegradable options when purchasing new ones.", "type": "non-recyclable"},
    "plastic_water_bottles": {"recommendation": "Rinse the bottle to ensure cleanliness. Recycle the bottle along with the cap if accepted. Try to use reusable bottles to reduce plastic waste.", "type": "recyclable"},
    "shoes": {"recommendation": "Donate shoes that are still wearable to charities or thrift stores. For damaged or unusable shoes, check for textile recycling bins. Avoid discarding in general waste.", "type": "recyclable"},
    "steel_food_cans": {"recommendation": "Clean the can by removing all food residue. Place it in your recycling bin. Check for local recycling guidelines if needed.", "type": "recyclable"},
    "styrofoam_cups": {"recommendation": "Styrofoam is not recyclable in most areas. Dispose of it in general waste. Avoid using Styrofoam products whenever possible.", "type": "non-recyclable"},
    "styrofoam_food_containers": {"recommendation": "Clean the container before disposal if required. Place it in general waste as Styrofoam is typically non-recyclable. Consider switching to sustainable alternatives.", "type": "non-recyclable"},
    "tea_bags": {"recommendation": "Compost biodegradable tea bags as they are rich in organic matter. Check if your tea bags have plastic components and dispose of those in general waste.", "type": "organic"}
}


# Flask app setup
app = Flask(__name__)

# Endpoint to get disposal information based on keyword
@app.route('/process', methods=['GET'])
def get_disposal_info():
    # Extract the 'keyword' from the query parameters
    keyword = request.args.get('keyword', '').lower()  # Convert to lowercase to make the search case-insensitive
    
    # Lookup the keyword in the disposal methods dictionary
    disposal_info = disposal_methods.get(keyword)
    
    if not disposal_info:
        return jsonify({'error': 'No disposal information available for the provided keyword'}), 404
    
    return jsonify({
        "category": keyword,
        "disposal_recommendation": disposal_info["recommendation"],
        "type": disposal_info["type"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)