# `EGStillImageFusionGraph`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageGraph`
- Protocols: `EGStillImageTopLevelGraph`
- 5 instance variables, 5 properties, 2 instance methods, 2 class methods

## Instance variables

```
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"<BWStillImageProcessingCoordinatorDelegate>" _delegate;
@"NSMutableDictionary" _processorControllerSourceNodesByType;
```

## Properties

```
@property (T@"NSString",R,N) captureRequestIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageFusionGraph initialize];
+[EGStillImageFusionGraph isSupportedForSettings:nodeConfiguration:];
```

## Instance methods

```
-[EGStillImageFusionGraph dealloc];
-[EGStillImageFusionGraph initWithStillImageSettings:nodeConfiguration:resourceCoordinator:delegate:];
```
