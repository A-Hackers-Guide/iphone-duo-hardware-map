# `CoreMLModelSecurityServiceToClient`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreMLModelSecurityServiceToClientProtocol`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _featureProviderMap;
@"NSCountedSet" _featureProviderCount;
@"NSObject<OS_dispatch_queue>" _serviceToClientQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_featureProviderMap) featureProviderMap;
@property (T@"NSCountedSet",&,N,V_featureProviderCount) featureProviderCount;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_serviceToClientQueue) serviceToClientQueue;
```

## Instance methods

```
-[CoreMLModelSecurityServiceToClient init];
-[CoreMLModelSecurityServiceToClient clientFeatureNames:withReply:];
-[CoreMLModelSecurityServiceToClient clientFeatureValueForName:uniqueKeyForProvider:withReply:];
-[CoreMLModelSecurityServiceToClient featureProviderCount];
-[CoreMLModelSecurityServiceToClient featureProviderMap];
-[CoreMLModelSecurityServiceToClient serviceToClientQueue];
-[CoreMLModelSecurityServiceToClient setFeatureProviderCount:];
-[CoreMLModelSecurityServiceToClient setFeatureProviderMap:];
-[CoreMLModelSecurityServiceToClient setServiceToClientQueue:];
```
