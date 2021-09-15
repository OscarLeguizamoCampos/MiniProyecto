def solicitud_arrendamiento(solicitud: dict) -> dict:
    
    id_solicitud = solicitud['id_solicitud']
    documentos_completos = solicitud['documentos_completos']
    tipo_contrato = solicitud['tipo_contrato']
    valor_canon = solicitud['valor_canon']
    ingresos_solicitante = solicitud['ingresos_solicitante']
    ingresos_fiador = solicitud['ingresos_fiador']
    fiador_finca = solicitud['fiador_finca']
    finca_libre = solicitud['finca_libre']
    solicitante_reportado = solicitud['solicitante_reportado']
    fiador_reportado = solicitud['fiador_reportado']


    if (documentos_completos == 'NO'):
        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
    else:
        if (documentos_completos == 'SI'):
            if(solicitante_reportado == 'SI'):
                return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
            else:
                if(solicitante_reportado == 'NO'):
                    if(tipo_contrato == 'I' or tipo_contrato == 'D'):
                        if(valor_canon*2 <= ingresos_solicitante):
                            if (fiador_reportado == 'SI'):
                                return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                            else:
                                if (valor_canon*2 <= ingresos_fiador):
                                    return{'id_solicitud':id_solicitud, 'resultado_analisis':True}
                                else:
                                    return{'id_solicitud':id_solicitud, 'resultado_analisis':False}      
                        else:
                            if (fiador_reportado == 'SI'):
                                return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                            else:
                                if(fiador_finca == 'NO'):
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                                else:
                                    if (finca_libre == 'NO'):
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                                    if (valor_canon*2 <= ingresos_fiador):
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':True}
                                    else:
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}                                         
                    else:
                        if(tipo_contrato == 'P'):    
                            if (fiador_reportado == 'SI'):
                                return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                            else:
                                if(fiador_finca == 'NO'):
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                                else:
                                    if (finca_libre == 'NO'):
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}
                                    if (valor_canon*2 <= ingresos_fiador):
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':True}
                                    else:
                                        return{'id_solicitud':id_solicitud, 'resultado_analisis':False}        

    

solicitud = {
    'id_solicitud':'SLC01',
    'documentos_completos':'SI',
    'tipo_contrato':'I',
    'valor_canon':700000.67,
    'ingresos_solicitante': 1600000.00,
    'ingresos_fiador': 1600000.00,
    'fiador_finca': 'SI',
    'finca_libre': 'SI',
    'solicitante_reportado': 'NO',
    'fiador_reportado': 'NO'
}

print(solicitud_arrendamiento(solicitud))