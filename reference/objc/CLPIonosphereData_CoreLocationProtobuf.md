# `CLPIonosphereData`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 20 instance variables, 38 properties, 85 instance methods, 0 class methods

## Instance variables

```
d _applicableTimeSec;
d _d2vtecDphi2;
d _d2vtecDtheta2;
d _d2vtecDthetaphi;
d _dvtecDphi;
d _dvtecDtheta;
d _estimatorAgeSec;
d _geodeticAltitudeM;
d _hmaxKm;
d _latitudeDeg;
d _longitudeDeg;
d _pd2vtecDphi2D2vtecDphi2;
d _pd2vtecDtheta2D2vtecDtheta2;
d _pd2vtecDthetadphiD2vtecDthetadphi;
d _pdvtecDphiDvtecDphi;
d _pdvtecDthetaDvtecDtheta;
d _phmaxHmaxKm2;
d _pvtec0Vtec0;
d _vtec0;
{?="applicableTimeSec"b1"d2vtecDphi2"b1"d2vtecDtheta2"b1"d2vtecDthetaphi"b1"dvtecDphi"b1"dvtecDtheta"b1"estimatorAgeSec"b1"geodeticAltitudeM"b1"hmaxKm"b1"latitudeDeg"b1"longitudeDeg"b1"pd2vtecDphi2D2vtecDphi2"b1"pd2vtecDtheta2D2vtecDtheta2"b1"pd2vtecDthetadphiD2vtecDthetadphi"b1"pdvtecDphiDvtecDphi"b1"pdvtecDthetaDvtecDtheta"b1"phmaxHmaxKm2"b1"pvtec0Vtec0"b1"vtec0"b1} _has;
```

## Properties

```
@property (TB,N) hasLatitudeDeg;
@property (Td,N,V_latitudeDeg) latitudeDeg;
@property (TB,N) hasLongitudeDeg;
@property (Td,N,V_longitudeDeg) longitudeDeg;
@property (TB,N) hasGeodeticAltitudeM;
@property (Td,N,V_geodeticAltitudeM) geodeticAltitudeM;
@property (TB,N) hasApplicableTimeSec;
@property (Td,N,V_applicableTimeSec) applicableTimeSec;
@property (TB,N) hasHmaxKm;
@property (Td,N,V_hmaxKm) hmaxKm;
@property (TB,N) hasVtec0;
@property (Td,N,V_vtec0) vtec0;
@property (TB,N) hasDvtecDtheta;
@property (Td,N,V_dvtecDtheta) dvtecDtheta;
@property (TB,N) hasDvtecDphi;
@property (Td,N,V_dvtecDphi) dvtecDphi;
@property (TB,N) hasD2vtecDtheta2;
@property (Td,N,V_d2vtecDtheta2) d2vtecDtheta2;
@property (TB,N) hasD2vtecDthetaphi;
@property (Td,N,V_d2vtecDthetaphi) d2vtecDthetaphi;
@property (TB,N) hasD2vtecDphi2;
@property (Td,N,V_d2vtecDphi2) d2vtecDphi2;
@property (TB,N) hasEstimatorAgeSec;
@property (Td,N,V_estimatorAgeSec) estimatorAgeSec;
@property (TB,N) hasPhmaxHmaxKm2;
@property (Td,N,V_phmaxHmaxKm2) phmaxHmaxKm2;
@property (TB,N) hasPvtec0Vtec0;
@property (Td,N,V_pvtec0Vtec0) pvtec0Vtec0;
@property (TB,N) hasPdvtecDthetaDvtecDtheta;
@property (Td,N,V_pdvtecDthetaDvtecDtheta) pdvtecDthetaDvtecDtheta;
@property (TB,N) hasPdvtecDphiDvtecDphi;
@property (Td,N,V_pdvtecDphiDvtecDphi) pdvtecDphiDvtecDphi;
@property (TB,N) hasPd2vtecDtheta2D2vtecDtheta2;
@property (Td,N,V_pd2vtecDtheta2D2vtecDtheta2) pd2vtecDtheta2D2vtecDtheta2;
@property (TB,N) hasPd2vtecDthetadphiD2vtecDthetadphi;
@property (Td,N,V_pd2vtecDthetadphiD2vtecDthetadphi) pd2vtecDthetadphiD2vtecDthetadphi;
@property (TB,N) hasPd2vtecDphi2D2vtecDphi2;
@property (Td,N,V_pd2vtecDphi2D2vtecDphi2) pd2vtecDphi2D2vtecDphi2;
```

## Instance methods

```
-[CLPIonosphereData writeTo:];
-[CLPIonosphereData mergeFrom:];
-[CLPIonosphereData hash];
-[CLPIonosphereData copyTo:];
-[CLPIonosphereData description];
-[CLPIonosphereData readFrom:];
-[CLPIonosphereData copyWithZone:];
-[CLPIonosphereData isEqual:];
-[CLPIonosphereData dictionaryRepresentation];
-[CLPIonosphereData setLatitudeDeg:];
-[CLPIonosphereData latitudeDeg];
-[CLPIonosphereData longitudeDeg];
-[CLPIonosphereData setLongitudeDeg:];
-[CLPIonosphereData d2vtecDthetaphi];
-[CLPIonosphereData setDvtecDtheta:];
-[CLPIonosphereData setPd2vtecDtheta2D2vtecDtheta2:];
-[CLPIonosphereData setPvtec0Vtec0:];
-[CLPIonosphereData estimatorAgeSec];
-[CLPIonosphereData hasLongitudeDeg];
-[CLPIonosphereData hasPhmaxHmaxKm2];
-[CLPIonosphereData setD2vtecDphi2:];
-[CLPIonosphereData applicableTimeSec];
-[CLPIonosphereData d2vtecDphi2];
-[CLPIonosphereData d2vtecDtheta2];
-[CLPIonosphereData dvtecDphi];
-[CLPIonosphereData dvtecDtheta];
-[CLPIonosphereData geodeticAltitudeM];
-[CLPIonosphereData hasApplicableTimeSec];
-[CLPIonosphereData hasD2vtecDphi2];
-[CLPIonosphereData hasD2vtecDtheta2];
-[CLPIonosphereData hasD2vtecDthetaphi];
-[CLPIonosphereData hasDvtecDphi];
-[CLPIonosphereData hasDvtecDtheta];
-[CLPIonosphereData hasEstimatorAgeSec];
-[CLPIonosphereData hasGeodeticAltitudeM];
-[CLPIonosphereData hasHmaxKm];
-[CLPIonosphereData hasLatitudeDeg];
-[CLPIonosphereData hasPd2vtecDphi2D2vtecDphi2];
-[CLPIonosphereData hasPd2vtecDtheta2D2vtecDtheta2];
-[CLPIonosphereData hasPd2vtecDthetadphiD2vtecDthetadphi];
-[CLPIonosphereData hasPdvtecDphiDvtecDphi];
-[CLPIonosphereData hasPdvtecDthetaDvtecDtheta];
-[CLPIonosphereData hasPvtec0Vtec0];
-[CLPIonosphereData hasVtec0];
-[CLPIonosphereData hmaxKm];
-[CLPIonosphereData pd2vtecDphi2D2vtecDphi2];
-[CLPIonosphereData pd2vtecDtheta2D2vtecDtheta2];
-[CLPIonosphereData pd2vtecDthetadphiD2vtecDthetadphi];
-[CLPIonosphereData pdvtecDphiDvtecDphi];
-[CLPIonosphereData pdvtecDthetaDvtecDtheta];
-[CLPIonosphereData phmaxHmaxKm2];
-[CLPIonosphereData pvtec0Vtec0];
-[CLPIonosphereData setApplicableTimeSec:];
-[CLPIonosphereData setD2vtecDtheta2:];
-[CLPIonosphereData setD2vtecDthetaphi:];
-[CLPIonosphereData setDvtecDphi:];
-[CLPIonosphereData setEstimatorAgeSec:];
-[CLPIonosphereData setGeodeticAltitudeM:];
-[CLPIonosphereData setHasApplicableTimeSec:];
-[CLPIonosphereData setHasD2vtecDphi2:];
-[CLPIonosphereData setHasD2vtecDtheta2:];
-[CLPIonosphereData setHasD2vtecDthetaphi:];
-[CLPIonosphereData setHasDvtecDphi:];
-[CLPIonosphereData setHasDvtecDtheta:];
-[CLPIonosphereData setHasEstimatorAgeSec:];
-[CLPIonosphereData setHasGeodeticAltitudeM:];
-[CLPIonosphereData setHasHmaxKm:];
-[CLPIonosphereData setHasLatitudeDeg:];
-[CLPIonosphereData setHasLongitudeDeg:];
-[CLPIonosphereData setHasPd2vtecDphi2D2vtecDphi2:];
-[CLPIonosphereData setHasPd2vtecDtheta2D2vtecDtheta2:];
-[CLPIonosphereData setHasPd2vtecDthetadphiD2vtecDthetadphi:];
-[CLPIonosphereData setHasPdvtecDphiDvtecDphi:];
-[CLPIonosphereData setHasPdvtecDthetaDvtecDtheta:];
-[CLPIonosphereData setHasPhmaxHmaxKm2:];
-[CLPIonosphereData setHasPvtec0Vtec0:];
-[CLPIonosphereData setHasVtec0:];
-[CLPIonosphereData setHmaxKm:];
-[CLPIonosphereData setPd2vtecDphi2D2vtecDphi2:];
-[CLPIonosphereData setPd2vtecDthetadphiD2vtecDthetadphi:];
-[CLPIonosphereData setPdvtecDphiDvtecDphi:];
-[CLPIonosphereData setPdvtecDthetaDvtecDtheta:];
-[CLPIonosphereData setPhmaxHmaxKm2:];
-[CLPIonosphereData setVtec0:];
-[CLPIonosphereData vtec0];
```
