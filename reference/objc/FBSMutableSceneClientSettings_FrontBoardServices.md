# `FBSMutableSceneClientSettings`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneClientSettings`
- Protocols: `FBSMutableSettings`
- 0 instance variables, 9 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"NSOrderedSet",C,D,N) layers;
@property (Td,D,N) preferredLevel;
@property (Tq,D,N) preferredInterfaceOrientation;
@property (T@"NSString",C,D,N) preferredSceneHostIdentifier;
@property (T@"FBSSceneIdentityToken",C,D,N) preferredSceneHostIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSMutableSceneClientSettings addLayer:];
-[FBSMutableSceneClientSettings removeLayer:];
-[FBSMutableSceneClientSettings removeAllLayers];
-[FBSMutableSceneClientSettings _applySafeValuesFromUntrustedSettings:];
```
