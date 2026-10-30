# `SBSACalloutBlockAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAActionRepresenting`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _reasons;
@? _calloutBlock;
```

## Properties

```
@property (T@?,R,C,N,V_calloutBlock) calloutBlock;
@property (T@"NSArray",R,C,N,V_reasons) reasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSACalloutBlockAction initialize];
```

## Instance methods

```
-[SBSACalloutBlockAction reasons];
-[SBSACalloutBlockAction encodeWithCoder:];
-[SBSACalloutBlockAction hash];
-[SBSACalloutBlockAction description];
-[SBSACalloutBlockAction copyWithZone:];
-[SBSACalloutBlockAction isEqual:];
-[SBSACalloutBlockAction membersForCoder];
-[SBSACalloutBlockAction calloutBlock];
-[SBSACalloutBlockAction initWithCalloutBlock:reasons:];
```
