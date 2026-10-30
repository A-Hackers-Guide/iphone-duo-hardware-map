# `UIWritingToolsCoordinatorGrammarItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIWritingToolsCoordinatorContext" _context;
@"NSAttributedString" _originalAttributedString;
@"WTTextSuggestion" _suggestion;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (T@"UIWritingToolsCoordinatorContext",R,N,V_context) context;
@property (T{_NSRange=QQ},N,V_range) range;
@property (T@"NSAttributedString",R,C,N,V_originalAttributedString) originalAttributedString;
@property (T@"WTTextSuggestion",R,N,V_suggestion) suggestion;
```

## Instance methods

```
-[UIWritingToolsCoordinatorGrammarItem suggestion];
-[UIWritingToolsCoordinatorGrammarItem range];
-[UIWritingToolsCoordinatorGrammarItem setRange:];
-[UIWritingToolsCoordinatorGrammarItem description];
-[UIWritingToolsCoordinatorGrammarItem context];
-[UIWritingToolsCoordinatorGrammarItem initWithRange:inContext:];
-[UIWritingToolsCoordinatorGrammarItem initWithSuggestion:inContext:];
-[UIWritingToolsCoordinatorGrammarItem originalAttributedString];
```
