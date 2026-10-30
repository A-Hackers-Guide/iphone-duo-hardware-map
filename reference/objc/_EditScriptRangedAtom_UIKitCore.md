# `_EditScriptRangedAtom`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSString" _replacementText;
{_NSRange="location"Q"length"Q} _editRange;
```

## Properties

```
@property (T{_NSRange=QQ},N,V_editRange) editRange;
@property (T@"NSString",&,N,V_replacementText) replacementText;
```

## Class methods

```
+[_EditScriptRangedAtom atomWithEditRange:replacementText:];
```

## Instance methods

```
-[_EditScriptRangedAtom replacementText];
-[_EditScriptRangedAtom setReplacementText:];
-[_EditScriptRangedAtom description];
-[_EditScriptRangedAtom editRange];
-[_EditScriptRangedAtom initWithEditRange:replacementText:];
-[_EditScriptRangedAtom setEditRange:];
```
