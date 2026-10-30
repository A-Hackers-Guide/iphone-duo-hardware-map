# `SDUDisplayBlankingDescription`

- Image: [`/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`](../userland/System__Library__PrivateFrameworks__SystemUIDisplayUtilities.framework__SystemUIDisplayUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _regionIdentifier;
Q _blankingState;
@"NSArray" _bundleIDs;
Q _previousBlankingState;
@"NSArray" _previousBundleIDs;
```

## Properties

```
@property (T@"NSString",R,C,N,V_regionIdentifier) regionIdentifier;
@property (TQ,R,N,V_blankingState) blankingState;
@property (T@"NSArray",R,C,N,V_bundleIDs) bundleIDs;
@property (TQ,R,N,V_previousBlankingState) previousBlankingState;
@property (T@"NSArray",R,C,N,V_previousBundleIDs) previousBundleIDs;
```

## Instance methods

```
-[SDUDisplayBlankingDescription bundleIDs];
-[SDUDisplayBlankingDescription regionIdentifier];
-[SDUDisplayBlankingDescription blankingState];
-[SDUDisplayBlankingDescription initWithRegionIdentifier:blankingState:bundleIDs:previousBlankingState:previousBundleIDs:];
-[SDUDisplayBlankingDescription previousBlankingState];
-[SDUDisplayBlankingDescription previousBundleIDs];
```
