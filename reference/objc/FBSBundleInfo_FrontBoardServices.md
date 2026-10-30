# `FBSBundleInfo`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSString" _displayName;
@"NSString" _bundleIdentifier;
@"NSString" _bundleVersion;
@"NSString" _bundleType;
@"NSURL" _bundleURL;
Q _sequenceNumber;
@"NSUUID" _cacheGUID;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSURL",R,N,V_bundleURL) bundleURL;
@property (T@"NSString",R,C,N,V_displayName) displayName;
@property (T@"NSString",R,C,N,V_bundleVersion) bundleVersion;
@property (T@"NSString",R,C,N,V_bundleType) bundleType;
@property (TQ,R,N,V_sequenceNumber) sequenceNumber;
@property (T@"NSUUID",R,C,N,V_cacheGUID) cacheGUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSBundleInfo bundleVersion];
-[FBSBundleInfo bundleURL];
-[FBSBundleInfo debugDescription];
-[FBSBundleInfo succinctDescriptionBuilder];
-[FBSBundleInfo init];
-[FBSBundleInfo displayName];
-[FBSBundleInfo sequenceNumber];
-[FBSBundleInfo bundleType];
-[FBSBundleInfo bundleIdentifier];
-[FBSBundleInfo descriptionWithMultilinePrefix:];
-[FBSBundleInfo succinctDescription];
-[FBSBundleInfo description];
-[FBSBundleInfo descriptionBuilderWithMultilinePrefix:];
-[FBSBundleInfo cacheGUID];
-[FBSBundleInfo _initWithBundleIdentifier:url:];
-[FBSBundleInfo _initWithBundleProxy:bundleIdentifier:url:];
-[FBSBundleInfo _initWithBundleProxy:overrideURL:];
-[FBSBundleInfo applicationIdentity];
```
