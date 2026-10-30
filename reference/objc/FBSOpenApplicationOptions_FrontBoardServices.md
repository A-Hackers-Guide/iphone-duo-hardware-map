# `FBSOpenApplicationOptions`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSXPCSecureCoding`, `NSCopying`
- 1 instance variables, 7 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _payload;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_payload) dictionary;
@property (T@"NSURL",R,N) url;
@property (T@"NSSet",R,N) actions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSOpenApplicationOptions supportsBSXPCSecureCoding];
+[FBSOpenApplicationOptions optionsWithDictionary:];
```

## Instance methods

```
-[FBSOpenApplicationOptions setDictionary:];
-[FBSOpenApplicationOptions succinctDescriptionBuilder];
-[FBSOpenApplicationOptions initWithXPCDictionary:];
-[FBSOpenApplicationOptions dictionary];
-[FBSOpenApplicationOptions descriptionWithMultilinePrefix:];
-[FBSOpenApplicationOptions actions];
-[FBSOpenApplicationOptions succinctDescription];
-[FBSOpenApplicationOptions encodeWithXPCDictionary:];
-[FBSOpenApplicationOptions _sanitizeAndValidatePayload];
-[FBSOpenApplicationOptions description];
-[FBSOpenApplicationOptions encodeWithBSXPCCoder:];
-[FBSOpenApplicationOptions initWithBSXPCCoder:];
-[FBSOpenApplicationOptions copyWithZone:];
-[FBSOpenApplicationOptions _updateOption:forKey:];
-[FBSOpenApplicationOptions url];
-[FBSOpenApplicationOptions descriptionBuilderWithMultilinePrefix:];
```
