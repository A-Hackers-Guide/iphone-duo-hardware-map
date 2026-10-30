# `MLState`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _featureProviderRepresentationCacheLock;
@"<MLFeatureProvider>" _featureProviderRepresentationCache;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateBuffersLock;
@"NSDictionary" _backings;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_backings) backings;
@property (T@"<MLFeatureProvider>",R,C,N) featureProviderRepresentation;
```

## Class methods

```
+[MLState emptyState];
```

## Instance methods

```
-[MLState description];
-[MLState backings];
-[MLState featureProviderRepresentation];
-[MLState getMultiArrayForStateNamed:handler:];
-[MLState getMultiArrayWithHandler:];
-[MLState initWithBackings:];
-[MLState internalGetMultiArrayWithHandler:];
```
