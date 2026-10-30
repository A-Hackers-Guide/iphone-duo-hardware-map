# `FBSShutdownOptions`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`
- 5 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reason;
q _rebootType;
q _source;
q _LPEMOption;
@"<NSCopying>" _localContext;
```

## Properties

```
@property (Tq,N,V_LPEMOption) LPEMOption;
@property (T@"<NSCopying>",W,N,V_localContext) localContext;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (Tq,N,V_rebootType) rebootType;
@property (Tq,N,V_source) source;
@property (TB,R,N) isShutdown;
@property (TB,R,N) isReboot;
@property (TB,R,N) isUserInitiated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSShutdownOptions isShutdown];
-[FBSShutdownOptions succinctDescriptionBuilder];
-[FBSShutdownOptions init];
-[FBSShutdownOptions initWithXPCDictionary:];
-[FBSShutdownOptions initWithReason:];
-[FBSShutdownOptions descriptionWithMultilinePrefix:];
-[FBSShutdownOptions localContext];
-[FBSShutdownOptions setSource:];
-[FBSShutdownOptions succinctDescription];
-[FBSShutdownOptions encodeWithXPCDictionary:];
-[FBSShutdownOptions isUserInitiated];
-[FBSShutdownOptions description];
-[FBSShutdownOptions reason];
-[FBSShutdownOptions copyWithZone:];
-[FBSShutdownOptions source];
-[FBSShutdownOptions descriptionBuilderWithMultilinePrefix:];
-[FBSShutdownOptions setLocalContext:];
-[FBSShutdownOptions LPEMOption];
-[FBSShutdownOptions isReboot];
-[FBSShutdownOptions rebootType];
-[FBSShutdownOptions setLPEMOption:];
-[FBSShutdownOptions setRebootType:];
```
