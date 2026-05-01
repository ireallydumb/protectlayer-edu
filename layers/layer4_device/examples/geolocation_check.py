#!/usr/bin/env python3
"""
Layer 4, Example 2: Geo-IP Restriction

Block access based on geographic location.

Used by: Streaming services, regional licensing systems
"""

import socket

def get_ip_geolocation(ip_address):
    """
    Get approximate location from IP (requires external API)
    
    Free services:
    - ip-api.com (45 requests/minute)
    - ipapi.co (30 requests/day free)
    - geoip.db (local database)
    
    Args:
        ip_address: IP to geolocate
        
    Returns:
        {'country': 'US', 'region': 'CA', 'city': 'Los Angeles'}
    """
    try:
        import requests
        response = requests.get(f'https://ip-api.com/json/{ip_address}')
        data = response.json()
        return {
            'country': data.get('countryCode'),
            'region': data.get('region'),
            'city': data.get('city')
        }
    except:
        return None

def check_location_allowed(ip_address, allowed_countries=['US', 'CA']):
    """Check if location is in allowed list"""
    geo = get_ip_geolocation(ip_address)
    if geo and geo['country'] in allowed_countries:
        return True, geo
    return False, geo

if __name__ == "__main__":
    print("Geo-IP restriction example")
    print("Used for: Regional licensing, content restrictions")
