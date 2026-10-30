# `EspressoDCNEspressoOverfeatDetector`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
i tileSizeScaleFactor;
i tileDimension;
i localFaceMerging;
^v face_list;
@"EspressoFDOverfeatNetwork" _enet;
d _confidenceThreshold;
d _minBoundingBoxThreshold;
```

## Properties

```
@property (T@"EspressoFDOverfeatNetwork",&,N,V_enet) enet;
@property (Td,N,V_confidenceThreshold) confidenceThreshold;
@property (Td,N,V_minBoundingBoxThreshold) minBoundingBoxThreshold;
```

## Instance methods

```
-[EspressoDCNEspressoOverfeatDetector commonInit];
-[EspressoDCNEspressoOverfeatDetector init];
-[EspressoDCNEspressoOverfeatDetector dealloc];
-[EspressoDCNEspressoOverfeatDetector initWithOptions:];
-[EspressoDCNEspressoOverfeatDetector initWithNetwork:];
-[EspressoDCNEspressoOverfeatDetector compareObject:withObject:error:];
-[EspressoDCNEspressoOverfeatDetector computeBBoxUsingProb:box:andScalefactor:padX:padY:];
-[EspressoDCNEspressoOverfeatDetector confidenceThreshold];
-[EspressoDCNEspressoOverfeatDetector enet];
-[EspressoDCNEspressoOverfeatDetector fillFaceList];
-[EspressoDCNEspressoOverfeatDetector getDescription];
-[EspressoDCNEspressoOverfeatDetector getFacesFromNetworkResultOriginalWidth:originalHeight:];
-[EspressoDCNEspressoOverfeatDetector mergeFaceList];
-[EspressoDCNEspressoOverfeatDetector minBoundingBoxThreshold];
-[EspressoDCNEspressoOverfeatDetector setConfidenceThreshold:];
-[EspressoDCNEspressoOverfeatDetector setEnet:];
-[EspressoDCNEspressoOverfeatDetector setMinBoundingBoxThreshold:];
```
