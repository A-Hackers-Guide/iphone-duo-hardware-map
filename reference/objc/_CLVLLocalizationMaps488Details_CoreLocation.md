# `_CLVLLocalizationMaps488Details`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 20 instance variables, 20 properties, 35 instance methods, 1 class methods

## Instance variables

```
[6d] _slamOrigin;
[3[3d]] _resultPoseRotation;
[3d] _resultPoseTranslation;
Q _inliersCount;
^f _points2D;
^d _points3D;
^i _inlierIndices;
Q _slamTracksCount;
^f _slamTracks;
Q _descriptorDimension;
* _slamTrackDescriptors;
^s _slamTrackObservations;
Q _totalObservationsCount;
^f _slamTracks2D;
^s _slamTrackImageIndices;
Q _frameCount;
^i _perFrameVioStatusCodes;
^f _perFrameVioPoses;
^f _perFrameCalibrationMatrices;
^f _perFrameDistortion;
```

## Properties

```
@property (TQ,R,N,V_inliersCount) inliersCount;
@property (T^f,R,N,V_points2D) points2D;
@property (T^d,R,N,V_points3D) points3D;
@property (T^i,R,N,V_inlierIndices) inlierIndices;
@property (T^d,R,N) slamOrigin;
@property (TQ,R,N,V_slamTracksCount) slamTracksCount;
@property (T^f,R,N,V_slamTracks) slamTracks;
@property (TQ,R,N,V_descriptorDimension) descriptorDimension;
@property (T*,R,N,V_slamTrackDescriptors) slamTrackDescriptors;
@property (T^s,R,N,V_slamTrackObservations) slamTrackObservations;
@property (TQ,R,N,V_totalObservationsCount) totalObservationsCount;
@property (T^f,R,N,V_slamTracks2D) slamTracks2D;
@property (T^s,R,N,V_slamTrackImageIndices) slamTrackImageIndices;
@property (TQ,R,N,V_frameCount) frameCount;
@property (T^i,R,N,V_perFrameVioStatusCodes) perFrameVioStatusCodes;
@property (T^f,R,N,V_perFrameVioPoses) perFrameVioPoses;
@property (T^f,R,N,V_perFrameCalibrationMatrices) perFrameCalibrationMatrices;
@property (T^f,R,N,V_perFrameDistortion) perFrameDistortion;
@property (T^d,R,N) resultPoseRotation;
@property (T^d,R,N) resultPoseTranslation;
```

## Class methods

```
+[_CLVLLocalizationMaps488Details supportsSecureCoding];
```

## Instance methods

```
-[_CLVLLocalizationMaps488Details frameCount];
-[_CLVLLocalizationMaps488Details dealloc];
-[_CLVLLocalizationMaps488Details encodeWithCoder:];
-[_CLVLLocalizationMaps488Details description];
-[_CLVLLocalizationMaps488Details initWithCoder:];
-[_CLVLLocalizationMaps488Details copyWithZone:];
-[_CLVLLocalizationMaps488Details slamTracksCount];
-[_CLVLLocalizationMaps488Details slamTracks];
-[_CLVLLocalizationMaps488Details resetSlamTracks];
-[_CLVLLocalizationMaps488Details descriptionWithMemberIndent:endIndent:];
-[_CLVLLocalizationMaps488Details descriptorDimension];
-[_CLVLLocalizationMaps488Details inlierIndices];
-[_CLVLLocalizationMaps488Details inliersCount];
-[_CLVLLocalizationMaps488Details perFrameCalibrationMatrices];
-[_CLVLLocalizationMaps488Details perFrameDistortion];
-[_CLVLLocalizationMaps488Details perFrameVioPoses];
-[_CLVLLocalizationMaps488Details perFrameVioStatusCodes];
-[_CLVLLocalizationMaps488Details points2D];
-[_CLVLLocalizationMaps488Details points3D];
-[_CLVLLocalizationMaps488Details resetFrames];
-[_CLVLLocalizationMaps488Details resetInliers];
-[_CLVLLocalizationMaps488Details resultPoseRotation];
-[_CLVLLocalizationMaps488Details resultPoseTranslation];
-[_CLVLLocalizationMaps488Details setFrameCount:perFrameVioStatusCodes:perFrameVioPoses:perFrameCalibrationMatrices:perFrameDistortion:];
-[_CLVLLocalizationMaps488Details setInliersCount:points2D:points3D:inlierIndices:];
-[_CLVLLocalizationMaps488Details setResultPoseRotation:];
-[_CLVLLocalizationMaps488Details setResultPoseTranslation:];
-[_CLVLLocalizationMaps488Details setSlamOrigin:];
-[_CLVLLocalizationMaps488Details setSlamTracksCount:slamTracks:descriptorDimension:slamTrackDescriptors:slamTrackObservations:slamTracks2D:slamTrackImageIndices:];
-[_CLVLLocalizationMaps488Details slamOrigin];
-[_CLVLLocalizationMaps488Details slamTrackDescriptors];
-[_CLVLLocalizationMaps488Details slamTrackImageIndices];
-[_CLVLLocalizationMaps488Details slamTrackObservations];
-[_CLVLLocalizationMaps488Details slamTracks2D];
-[_CLVLLocalizationMaps488Details totalObservationsCount];
```
