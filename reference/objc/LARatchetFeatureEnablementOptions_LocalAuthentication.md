# `LARatchetFeatureEnablementOptions`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B isGracePeriodEnabled;
B isStrictModeEnabled;
B isExtendedPolicyModeEnabled;
B isAutoEnablement;
q source;
```

## Properties

```
@property (TB,N,VisGracePeriodEnabled) isGracePeriodEnabled;
@property (TB,N,VisStrictModeEnabled) isStrictModeEnabled;
@property (TB,N,VisExtendedPolicyModeEnabled) isExtendedPolicyModeEnabled;
@property (TB,N,VisAutoEnablement) isAutoEnablement;
@property (Tq,N,Vsource) source;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[LARatchetFeatureEnablementOptions initWithSource:];
-[LARatchetFeatureEnablementOptions isStrictModeEnabled];
-[LARatchetFeatureEnablementOptions init];
-[LARatchetFeatureEnablementOptions setIsStrictModeEnabled:];
-[LARatchetFeatureEnablementOptions setSource:];
-[LARatchetFeatureEnablementOptions description];
-[LARatchetFeatureEnablementOptions isEqual:];
-[LARatchetFeatureEnablementOptions source];
-[LARatchetFeatureEnablementOptions setIsExtendedPolicyModeEnabled:];
-[LARatchetFeatureEnablementOptions isAutoEnablement];
-[LARatchetFeatureEnablementOptions isExtendedPolicyModeEnabled];
-[LARatchetFeatureEnablementOptions isGracePeriodEnabled];
-[LARatchetFeatureEnablementOptions setIsAutoEnablement:];
-[LARatchetFeatureEnablementOptions setIsGracePeriodEnabled:];
```
