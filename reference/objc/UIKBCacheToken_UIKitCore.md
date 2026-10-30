# `UIKBCacheToken`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 11 properties, 39 instance methods, 7 class methods

## Instance variables

```
@"NSMutableArray" _components;
@"NSString" _name;
d _scale;
i _emptyFields;
@"NSSet" _transformationIdentifiers;
q _renderFlags;
```

## Properties

```
@property (T@"NSString",R,N) string;
@property (T{CGSize=dd},N) size;
@property (T@"NSString",&,N,V_name) name;
@property (Td,N,V_scale) scale;
@property (Ti,N) rowHint;
@property (Ti,N) displayHint;
@property (Tq,N,V_renderFlags) renderFlags;
@property (T{?=b6b1b1b8b8b8},N) styling;
@property (Ti,N,V_emptyFields) emptyFields;
@property (TB,R,N) hasKey;
@property (T@"NSSet",&,N,V_transformationIdentifiers) transformationIdentifiers;
```

## Class methods

```
+[UIKBCacheToken tokenForKey:style:renderConfig:];
+[UIKBCacheToken tokenForKey:style:renderConfig:displayInsets:];
+[UIKBCacheToken tokenForKeyMask:style:renderConfig:displayInsets:];
+[UIKBCacheToken tokenForKeyplane:renderConfig:];
+[UIKBCacheToken tokenTemplateFilledForKey:style:renderConfig:size:];
+[UIKBCacheToken tokenTemplateForKey:name:style:renderConfig:size:];
+[UIKBCacheToken tokenTemplateForKey:style:renderConfig:size:];
```

## Instance methods

```
-[UIKBCacheToken stringForState:];
-[UIKBCacheToken initWithComponents:name:];
-[UIKBCacheToken emptyFields];
-[UIKBCacheToken rowHint];
-[UIKBCacheToken renderFlags];
-[UIKBCacheToken setRowHint:];
-[UIKBCacheToken _writeString:toStr:maxLen:];
-[UIKBCacheToken displayHint];
-[UIKBCacheToken _writeArray:toStr:maxLen:];
-[UIKBCacheToken string];
-[UIKBCacheToken setScale:];
-[UIKBCacheToken resetAnnotations];
-[UIKBCacheToken size];
-[UIKBCacheToken scale];
-[UIKBCacheToken _writeNumber:toStr:];
-[UIKBCacheToken stringForComponentArray:additionalValues:];
-[UIKBCacheToken annotateWithBool:];
-[UIKBCacheToken setTransformationIdentifiers:];
-[UIKBCacheToken stringForConstruction:];
-[UIKBCacheToken _writeEdgeInsets:toStr:maxLen:];
-[UIKBCacheToken isUsableForCacheToken:withRenderFlags:];
-[UIKBCacheToken stringForKey:state:];
-[UIKBCacheToken stringForSplitState:handBias:];
-[UIKBCacheToken description];
-[UIKBCacheToken setName:];
-[UIKBCacheToken annotateWithInt:];
-[UIKBCacheToken transformationIdentifiers];
-[UIKBCacheToken copyWithZone:];
-[UIKBCacheToken styling];
-[UIKBCacheToken setDisplayHint:];
-[UIKBCacheToken stringForRenderFlags:renderConfig:];
-[UIKBCacheToken setRenderFlags:];
-[UIKBCacheToken copyTokenWithoutContentProperties];
-[UIKBCacheToken name];
-[UIKBCacheToken hasKey];
-[UIKBCacheToken setEmptyFields:];
-[UIKBCacheToken setStyling:];
-[UIKBCacheToken initWithName:];
-[UIKBCacheToken setSize:];
```
