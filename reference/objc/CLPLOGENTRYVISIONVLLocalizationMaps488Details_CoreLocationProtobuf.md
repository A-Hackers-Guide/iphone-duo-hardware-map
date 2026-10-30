# `CLPLOGENTRYVISIONVLLocalizationMaps488Details`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 20 instance variables, 38 properties, 113 instance methods, 0 class methods

## Instance variables

```
{?="list"^i"count"Q"size"Q} _inlierIndices;
{?="list"^f"count"Q"size"Q} _perFrameCalibrationMatrices;
{?="list"^f"count"Q"size"Q} _perFrameDistortions;
{?="list"^f"count"Q"size"Q} _perFrameVioPoses;
{?="list"^i"count"Q"size"Q} _perFrameVioStatusCodes;
{?="list"^f"count"Q"size"Q} _points2ds;
{?="list"^d"count"Q"size"Q} _points3ds;
{?="list"^d"count"Q"size"Q} _resultPoseRotations;
{?="list"^d"count"Q"size"Q} _resultPoseTranslations;
{?="list"^d"count"Q"size"Q} _slamOrigins;
{?="list"^i"count"Q"size"Q} _slamTrackImageIndices;
{?="list"^i"count"Q"size"Q} _slamTrackObservations;
{?="list"^f"count"Q"size"Q} _slamTracks;
{?="list"^f"count"Q"size"Q} _slamTracks2ds;
Q _descriptorDimension;
Q _numFrames;
Q _numInliers;
Q _numSlamTracks;
@"NSData" _slamTrackDescriptors;
{?="descriptorDimension"b1"numFrames"b1"numInliers"b1"numSlamTracks"b1} _has;
```

## Properties

```
@property (TB,N) hasNumInliers;
@property (TQ,N,V_numInliers) numInliers;
@property (TQ,R,N) points2dsCount;
@property (T^f,R,N) points2ds;
@property (TQ,R,N) points3dsCount;
@property (T^d,R,N) points3ds;
@property (TQ,R,N) inlierIndicesCount;
@property (T^i,R,N) inlierIndices;
@property (TQ,R,N) slamOriginsCount;
@property (T^d,R,N) slamOrigins;
@property (TB,N) hasNumSlamTracks;
@property (TQ,N,V_numSlamTracks) numSlamTracks;
@property (TQ,R,N) slamTracksCount;
@property (T^f,R,N) slamTracks;
@property (TB,N) hasDescriptorDimension;
@property (TQ,N,V_descriptorDimension) descriptorDimension;
@property (TB,R,N) hasSlamTrackDescriptors;
@property (T@"NSData",&,N,V_slamTrackDescriptors) slamTrackDescriptors;
@property (TQ,R,N) slamTrackObservationsCount;
@property (T^i,R,N) slamTrackObservations;
@property (TQ,R,N) slamTracks2dsCount;
@property (T^f,R,N) slamTracks2ds;
@property (TQ,R,N) slamTrackImageIndicesCount;
@property (T^i,R,N) slamTrackImageIndices;
@property (TB,N) hasNumFrames;
@property (TQ,N,V_numFrames) numFrames;
@property (TQ,R,N) perFrameVioStatusCodesCount;
@property (T^i,R,N) perFrameVioStatusCodes;
@property (TQ,R,N) perFrameVioPosesCount;
@property (T^f,R,N) perFrameVioPoses;
@property (TQ,R,N) perFrameCalibrationMatricesCount;
@property (T^f,R,N) perFrameCalibrationMatrices;
@property (TQ,R,N) perFrameDistortionsCount;
@property (T^f,R,N) perFrameDistortions;
@property (TQ,R,N) resultPoseRotationsCount;
@property (T^d,R,N) resultPoseRotations;
@property (TQ,R,N) resultPoseTranslationsCount;
@property (T^d,R,N) resultPoseTranslations;
```

## Instance methods

```
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details writeTo:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details mergeFrom:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details dealloc];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details hash];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details copyTo:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details description];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details readFrom:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details copyWithZone:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details isEqual:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details dictionaryRepresentation];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTracksCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearSlamTracks];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addResultPoseRotation:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addSlamOrigin:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addSlamTracks:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearResultPoseRotations];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearSlamOrigins];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details resultPoseRotationAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details resultPoseRotations];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details resultPoseRotationsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setResultPoseRotations:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setSlamOrigins:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamOriginAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamOrigins];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamOriginsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTracks];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTracksAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details descriptorDimension];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details inlierIndices];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameCalibrationMatrices];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameVioPoses];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameVioStatusCodes];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackDescriptors];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackImageIndices];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackObservations];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details numFrames];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setNumFrames:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addPerFrameCalibrationMatrices:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setSlamTrackImageIndices:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setSlamTrackObservations:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addInlierIndices:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addPerFrameDistortion:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addPerFrameVioPoses:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addPerFrameVioStatusCodes:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addPoints2d:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addPoints3d:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addResultPoseTranslation:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addSlamTrackImageIndices:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addSlamTrackObservations:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details addSlamTracks2d:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearInlierIndices];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearPerFrameCalibrationMatrices];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearPerFrameDistortions];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearPerFrameVioPoses];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearPerFrameVioStatusCodes];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearPoints2ds];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearPoints3ds];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearResultPoseTranslations];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearSlamTrackImageIndices];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearSlamTrackObservations];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details clearSlamTracks2ds];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details hasDescriptorDimension];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details hasNumFrames];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details hasNumInliers];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details hasNumSlamTracks];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details hasSlamTrackDescriptors];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details inlierIndicesAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details inlierIndicesCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details numInliers];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details numSlamTracks];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameCalibrationMatricesAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameCalibrationMatricesCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameDistortionAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameDistortions];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameDistortionsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameVioPosesAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameVioPosesCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameVioStatusCodesAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details perFrameVioStatusCodesCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details points2dAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details points2ds];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details points2dsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details points3dAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details points3ds];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details points3dsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details resultPoseTranslationAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details resultPoseTranslations];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details resultPoseTranslationsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setDescriptorDimension:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setHasDescriptorDimension:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setHasNumFrames:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setHasNumInliers:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setHasNumSlamTracks:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setInlierIndices:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setNumInliers:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setNumSlamTracks:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setPerFrameCalibrationMatrices:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setPerFrameDistortions:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setPerFrameVioPoses:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setPerFrameVioStatusCodes:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setPoints2ds:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setPoints3ds:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setResultPoseTranslations:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setSlamTrackDescriptors:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setSlamTracks2ds:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details setSlamTracks:count:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackImageIndicesAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackImageIndicesCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackObservationsAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTrackObservationsCount];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTracks2dAtIndex:];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTracks2ds];
-[CLPLOGENTRYVISIONVLLocalizationMaps488Details slamTracks2dsCount];
```
