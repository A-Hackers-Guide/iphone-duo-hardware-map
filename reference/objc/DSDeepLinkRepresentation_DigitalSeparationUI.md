# `DSDeepLinkRepresentation`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" _path;
B _flowRequiresAuth;
@"NSArray" _navigationOrder;
@"NSDictionary" _navigationChapters;
q _navigationType;
q _flowType;
@"NSString" _entrypoint;
```

## Properties

```
@property (T@"NSArray",R,N,V_navigationOrder) navigationOrder;
@property (T@"NSDictionary",R,N,V_navigationChapters) navigationChapters;
@property (Tq,R,N,V_navigationType) navigationType;
@property (TB,R,N,V_flowRequiresAuth) flowRequiresAuth;
@property (Tq,R,N,V_flowType) flowType;
@property (T@"NSString",R,N) remoteUIURL;
@property (T@"NSString",R,N,V_entrypoint) entrypoint;
```

## Instance methods

```
-[DSDeepLinkRepresentation navigationType];
-[DSDeepLinkRepresentation flowType];
-[DSDeepLinkRepresentation navigationOrder];
-[DSDeepLinkRepresentation entrypoint];
-[DSDeepLinkRepresentation flowRequiresAuth];
-[DSDeepLinkRepresentation initWithOrder:orderType:chapters:requiresAuth:flowType:entrypointAnalytic:path:];
-[DSDeepLinkRepresentation navigationChapters];
-[DSDeepLinkRepresentation remoteUIURL];
```
