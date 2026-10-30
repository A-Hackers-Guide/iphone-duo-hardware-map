# `_EditScriptDataArray`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_EditScriptData`
- 2 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _data;
@"NSString" _cachedStringValue;
```

## Properties

```
@property (T@"NSArray",&,N,V_data) data;
@property (T@"NSString",&,N,V_cachedStringValue) cachedStringValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_EditScriptDataArray EditScriptDataWithString:chunkSize:];
+[_EditScriptDataArray EditScriptDataWithArray:];
```

## Instance methods

```
-[_EditScriptDataArray stringValue];
-[_EditScriptDataArray data];
-[_EditScriptDataArray stringAtIndex:];
-[_EditScriptDataArray length];
-[_EditScriptDataArray initWithArray:];
-[_EditScriptDataArray setData:];
-[_EditScriptDataArray description];
-[_EditScriptDataArray cachedStringValue];
-[_EditScriptDataArray characterIndexForItem:];
-[_EditScriptDataArray indexOfFirstDifferenceWithOtherData:shouldReverseIterate:];
-[_EditScriptDataArray initWithString:chunkSize:];
-[_EditScriptDataArray lengthOfItem:];
-[_EditScriptDataArray setCachedStringValue:];
```
