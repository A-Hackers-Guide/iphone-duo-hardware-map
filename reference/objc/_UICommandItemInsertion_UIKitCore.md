# `_UICommandItemInsertion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UICommandChange`
- 3 instance variables, 4 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _fallbacks;
@"NSArray" _insertsBefore;
@"NSArray" _insertsAfter;
```

## Properties

```
@property (T@"_UICommandIdentifier",R,D,N) anchor;
@property (T@"NSArray",R,N,V_fallbacks) fallbacks;
@property (T@"NSArray",R,N,V_insertsBefore) insertsBefore;
@property (T@"NSArray",R,N,V_insertsAfter) insertsAfter;
```

## Class methods

```
+[_UICommandItemInsertion supportsSecureCoding];
+[_UICommandItemInsertion insertionWithAnchor:fallbacks:insertsBefore:insertsAfter:];
```

## Instance methods

```
-[_UICommandItemInsertion encodeWithCoder:];
-[_UICommandItemInsertion initWithCoder:];
-[_UICommandItemInsertion acceptBoolItemInsertionVisit:itemDeletionVisit:menuInsertionVisit:menuDeletionVisit:];
-[_UICommandItemInsertion acceptItemInsertionVisit:itemDeletionVisit:menuInsertionVisit:menuDeletionVisit:];
-[_UICommandItemInsertion fallbacks];
-[_UICommandItemInsertion initWithAnchor:fallbacks:insertsBefore:insertsAfter:];
-[_UICommandItemInsertion insertsAfter];
-[_UICommandItemInsertion insertsBefore];
```
