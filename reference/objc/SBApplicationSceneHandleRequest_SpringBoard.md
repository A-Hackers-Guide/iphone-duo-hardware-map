# `SBApplicationSceneHandleRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 3 class methods

## Instance variables

```
B _secure;
@"SBApplication" _application;
@"FBSDisplayIdentity" _displayIdentity;
@"FBSSceneDefinition" _sceneDefinition;
```

## Properties

```
@property (T@"SBApplication",&,N,V_application) application;
@property (T@"FBSDisplayIdentity",&,N,V_displayIdentity) displayIdentity;
@property (T@"FBSSceneDefinition",C,N,V_sceneDefinition) sceneDefinition;
@property (TB,N,GisSecure,V_secure) secure;
```

## Class methods

```
+[SBApplicationSceneHandleRequest defaultRequestForApplication:sceneIdentity:displayIdentity:];
+[SBApplicationSceneHandleRequest defaultRequestForApplication:sceneIdentity:displayIdentity:secure:];
+[SBApplicationSceneHandleRequest defaultSceneSpecificationForDisplayIdentity:secure:];
```

## Instance methods

```
-[SBApplicationSceneHandleRequest isSecure];
-[SBApplicationSceneHandleRequest setSecure:];
-[SBApplicationSceneHandleRequest application];
-[SBApplicationSceneHandleRequest setApplication:];
-[SBApplicationSceneHandleRequest displayIdentity];
-[SBApplicationSceneHandleRequest sceneDefinition];
-[SBApplicationSceneHandleRequest setSceneDefinition:];
-[SBApplicationSceneHandleRequest setDisplayIdentity:];
-[SBApplicationSceneHandleRequest initWithApplication:sceneDefinition:displayIdentity:];
```
