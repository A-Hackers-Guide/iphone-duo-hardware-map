# `_UIKeyboardInlineEmojiSearchController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`
- 9 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIResponder<UITextInput>" _inputDelegate;
@"UITableView" _tableView;
@"UIView" _tableContainer;
@"NSArray" _matches;
q _currentTokenLength;
@"NSDictionary" _emojiIndex;
@"UIView" _inputOverlayContainer;
@"NSObject<OS_dispatch_queue>" _searchQueue;
@"NSRegularExpression" _regularExpression;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardInlineEmojiSearchController tableView:numberOfRowsInSection:];
-[_UIKeyboardInlineEmojiSearchController hideSuggestions];
-[_UIKeyboardInlineEmojiSearchController tableView:cellForRowAtIndexPath:];
-[_UIKeyboardInlineEmojiSearchController init];
-[_UIKeyboardInlineEmojiSearchController tableView:didSelectRowAtIndexPath:];
-[_UIKeyboardInlineEmojiSearchController createViewsIfNeeded];
-[_UIKeyboardInlineEmojiSearchController currentEmojiQueryForContextBefore:];
-[_UIKeyboardInlineEmojiSearchController positionTableNearCaret];
-[_UIKeyboardInlineEmojiSearchController queueHidingSuggestions];
-[_UIKeyboardInlineEmojiSearchController updateWithInputDelegate:contextBefore:caretRect:inputOverlayContainer:];
```
