# Configuration

# Valuation Year and Quarter
VY = 2025
VQ = 1

# RBC Template and Output Paths
template_path = os.path.join('Demo', 'Template', 'HK RBC Disclosures.xlsx')
now_str = datetime.today().strftime('%Y%m%d_%H%M%S')
output_path = os.path.join('Demo', f'{VY}Q{VQ}', f'HK RBC Disclosures_{VY}Q{VQ}_{now_str}.xlsx')

#mySQL configuration
mysql_config = {
        'host': "",
        'user': "",
        'password': "",
        'port': 3306,
        'database': "",
        'pool_name': '',
        'pool_reset_session': 
    }