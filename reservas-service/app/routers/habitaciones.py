@router.put("/habitaciones/{id}/ocupar")
def ocupar_habitacion(id: int, db: Session = Depends(get_db)):
    habitacion = db.query(Habitacion).filter(Habitacion.id == id).first()

    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")

    habitacion.estado = "ocupada"
    db.commit()

    return {"message": "Habitación ocupada"}
