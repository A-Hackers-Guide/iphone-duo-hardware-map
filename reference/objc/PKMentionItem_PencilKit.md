# `PKMentionItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDetectionItem`
- 0 instance variables, 3 properties, 12 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,N) mentionResult;
@property (T@"NSUUID",R,N) mentionUUID;
@property (TB,R,N) active;
```

## Class methods

```
+[PKMentionItem mentionItemWithQueryItem:sessionManager:];
```

## Instance methods

```
-[PKMentionItem active];
-[PKMentionItem setActive:];
-[PKMentionItem strokeColor];
-[PKMentionItem hash];
-[PKMentionItem description];
-[PKMentionItem isEqual:];
-[PKMentionItem _actionNameForActivation:];
-[PKMentionItem _baselinePath];
-[PKMentionItem clearActiveInDrawing:];
-[PKMentionItem invalidateUUID];
-[PKMentionItem mentionResult];
-[PKMentionItem mentionUUID];
```
