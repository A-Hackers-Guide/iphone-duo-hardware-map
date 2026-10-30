# `UISApplicationInitializationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSMutableCopying`, `BSXPCSecureCoding`
- 7 instance variables, 12 properties, 21 instance methods, 2 class methods

## Instance variables

```
@"UISDisplayContext" _mainDisplayContext;
@"UISDisplayContext" _launchDisplayContext;
@"UISDeviceContext" _deviceContext;
@"UISCompatibilityContext" _compatibilityContext;
@"NSSet" _persistedSceneIdentifiers;
@"FBSSceneIdentityToken" _defaultSceneToken;
B _supportAppSceneRequests;
```

## Properties

```
@property (T@"UISDisplayContext",R,N) displayContext;
@property (T@"UISDisplayContext",R,N,V_mainDisplayContext) mainDisplayContext;
@property (T@"UISDisplayContext",R,N,V_launchDisplayContext) launchDisplayContext;
@property (T@"UISDeviceContext",R,N,V_deviceContext) deviceContext;
@property (T@"UISCompatibilityContext",R,N,V_compatibilityContext) compatibilityContext;
@property (T@"NSSet",R,N,V_persistedSceneIdentifiers) persistedSceneIdentifiers;
@property (T@"FBSSceneIdentityToken",R,N,V_defaultSceneToken) defaultSceneToken;
@property (TB,R,N,V_supportAppSceneRequests) supportAppSceneRequests;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISApplicationInitializationContext supportsBSXPCSecureCoding];
+[UISApplicationInitializationContext defaultContext];
```

## Instance methods

```
-[UISApplicationInitializationContext displayContext];
-[UISApplicationInitializationContext deviceContext];
-[UISApplicationInitializationContext mutableCopyWithZone:];
-[UISApplicationInitializationContext supportAppSceneRequests];
-[UISApplicationInitializationContext initWithXPCDictionary:];
-[UISApplicationInitializationContext initWithMainDisplayContext:launchDisplayContext:deviceContext:persistedSceneIdentifiers:supportAppSceneRequests:];
-[UISApplicationInitializationContext compatibilityContext];
-[UISApplicationInitializationContext persistedSceneIdentifiers];
-[UISApplicationInitializationContext initWithDisplayContext:deviceContext:persistedSceneIdentifiers:];
-[UISApplicationInitializationContext initWithUISApplicationInitializationContext:];
-[UISApplicationInitializationContext defaultSceneToken];
-[UISApplicationInitializationContext encodeWithXPCDictionary:];
-[UISApplicationInitializationContext launchDisplayContext];
-[UISApplicationInitializationContext hash];
-[UISApplicationInitializationContext description];
-[UISApplicationInitializationContext mainDisplayContext];
-[UISApplicationInitializationContext encodeWithBSXPCCoder:];
-[UISApplicationInitializationContext initWithBSXPCCoder:];
-[UISApplicationInitializationContext initWithDisplayContext:deviceContext:persistedSceneIdentifiers:supportAppSceneRequests:];
-[UISApplicationInitializationContext copyWithZone:];
-[UISApplicationInitializationContext isEqual:];
```
