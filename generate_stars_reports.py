"""
run_star_report_direct.py

Script de ejemplo que llama directamente a generate_star_report
sin usar argparse, con parámetros definidos en el propio código.
"""

from StellarPolAnalyzer.utils import run_star_report

def batch_generate_reports(report_list, output_dir):
    """
    Ejecuta run_star_report para cada entrada de report_list.

    Parámetros
    ----------
    report_list : list of tuples
        Lista de tuplas (json_path, simbad_id, filter_name).
    output_dir : str
        Carpeta donde se guardarán todos los reportes.
    """
    for json_path, simbad_id, filter_name in report_list:
        run_star_report(json_path, simbad_id, filter_name, output_dir)


if __name__ == '__main__':
    # Define aquí tu lista de reportes a generar
    report_list = [
        (
            'noche1_20230720_organize/1H1936+541/BessellI/reports/pipeline_results.json',
            '1H 1936+541',
            'I'
        ),
       (
           'noche1_20230720_organize/1H1936+541/BessellR/reports/pipeline_results.json',
           '1H 1936+541',
           'R'
       ),
       (
           'noche1_20230720_organize/1H1936+541/JohnsonV/reports/pipeline_results.json',
           '1H 1936+541',
           'V'
       ),
       
       (
           'noche1_20230720_organize/BD+384058/BessellI/reports/pipeline_results.json',
           'BD+38  4058',
           'I'
       ),
       (
           'noche1_20230720_organize/BD+384058/BessellR/reports/pipeline_results.json',
           'BD+38  4058',
           'R'
       ),
       (
           'noche1_20230720_organize/BD+384058/JohnsonB/reports/pipeline_results.json',
           'BD+38  4058',
           'B'
       ),
       (
           'noche1_20230720_organize/BD+384058/JohnsonV/reports/pipeline_results.json',
           'BD+38  4058',
           'V'
       ),
       
       (
           'noche1_20230720_organize/EXO2030+375/BessellI/reports/pipeline_results.json',
           'V* V2246 Cyg',
           'I'
       ),
       (
           'noche1_20230720_organize/EXO2030+375/BessellR/reports/pipeline_results.json',
           'V* V2246 Cyg',
           'R'
       ),
       
       (
           'noche1_20230720_organize/HD154892/BessellI/reports/pipeline_results.json',
           'HD 154892',
           'I'
       ),
       (
           'noche1_20230720_organize/HD154892/BessellR/reports/pipeline_results.json',
           'HD 154892',
           'R'
       ),
       
       (
           'noche1_20230720_organize/MWC656/BessellR/reports/pipeline_results.json',
           'HD 215227',
           'R'
       ),
       (
           'noche1_20230720_organize/MWC656/JohnsonB/reports/pipeline_results.json',
           'HD 215227',
           'B'
       ),
       
       (
           'noche1_20230720_organize/SS397/BessellI/reports/pipeline_results.json',
           'ATO J278.3657-10.5901',
           'I'
       ),
       (
           'noche1_20230720_organize/SS397/BessellR/reports/pipeline_results.json',
           'ATO J278.3657-10.5901',
           'R'
       ),
       (
           'noche1_20230720_organize/SS397/JohnsonB/reports/pipeline_results.json',
           'ATO J278.3657-10.5901',
           'B'
       ),
       (
           'noche1_20230720_organize/SS397/JohnsonV/reports/pipeline_results.json',
           'ATO J278.3657-10.5901',
           'V'
       ),
       
       (
           'noche1_20230720_organize/XMMJ183328/BessellI/reports/pipeline_results.json',
           'NGC  6649     9',
           'I'
       ),
       (
           'noche1_20230720_organize/XMMJ183328/BessellR/reports/pipeline_results.json',
           'NGC  6649     9',
           'R'
       ),
       (
           'noche1_20230720_organize/XMMJ183328/JohnsonB/reports/pipeline_results.json',
           'NGC  6649     9',
           'B'
       ),
       (
           'noche1_20230720_organize/XMMJ183328/JohnsonV/reports/pipeline_results.json',
           'NGC  6649     9',
           'V'
       ),
    ]
    output_dir = 'final_stars_reports'
    batch_generate_reports(report_list, output_dir)
    print('Todos los reportes han sido generados.')
