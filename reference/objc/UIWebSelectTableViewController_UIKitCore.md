# `UIWebSelectTableViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- Protocols: `UIKeyInput`
- 10 instance variables, 29 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"DOMHTMLSelectElement" _selectionNode;
@"NSArray" _cachedItems;
@"NSArray" _groupsAndOptions;
Q _singleSelectionIndex;
Q _singleSelectionSection;
B _allowsMultipleSelection;
d _fontSize;
d _maximumTextWidth;
q _textAlignment;
@"UIWebSelectPopover" _popover;
```

## Properties

```
@property (T@"DOMHTMLSelectElement",&,N,V_selectionNode) _selectionNode;
@property (T@"NSArray",&,N,V_groupsAndOptions) _groupsAndOptions;
@property (T@"NSArray",&,N,V_cachedItems) _cachedItems;
@property (T@"UIWebSelectPopover",N,V_popover) _popover;
@property (TB,R,N) hasText;
@property (Tq,?,N) autocapitalizationType;
@property (Tq,?,N) autocorrectionType;
@property (Tq,?,N) spellCheckingType;
@property (Tq,?,N) smartQuotesType;
@property (Tq,?,N) smartDashesType;
@property (Tq,?,N) smartInsertDeleteType;
@property (Tq,?,N) inlinePredictionType;
@property (Tq,?,N) mathExpressionCompletionType;
@property (Tq,?,N) grammarCheckingType;
@property (Tq,?,N) keyboardType;
@property (Tq,?,N) keyboardAppearance;
@property (Tq,?,N) returnKeyType;
@property (TB,?,N) enablesReturnKeyAutomatically;
@property (TB,?,N,GisSecureTextEntry) secureTextEntry;
@property (T@"NSString",?,C,N) textContentType;
@property (T@"UITextInputPasswordRules",?,C,N) passwordRules;
@property (Tq,?) writingToolsBehavior;
@property (TQ,?) allowedWritingToolsResultOptions;
@property (T@"UIConversationContext",?,&,N) conversationContext;
@property (TB,?,N) allowsNumberPadPopover;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebSelectTableViewController tableView:numberOfRowsInSection:];
-[UIWebSelectTableViewController numberOfSectionsInTableView:];
-[UIWebSelectTableViewController hasText];
-[UIWebSelectTableViewController tableView:cellForRowAtIndexPath:];
-[UIWebSelectTableViewController insertText:];
-[UIWebSelectTableViewController dealloc];
-[UIWebSelectTableViewController tableView:titleForHeaderInSection:];
-[UIWebSelectTableViewController viewWillAppear:];
-[UIWebSelectTableViewController _isEmpty];
-[UIWebSelectTableViewController tableView:didSelectRowAtIndexPath:];
-[UIWebSelectTableViewController deleteBackward];
-[UIWebSelectTableViewController _cachedItems];
-[UIWebSelectTableViewController _groupsAndOptions];
-[UIWebSelectTableViewController _optionsForSection:];
-[UIWebSelectTableViewController _popover];
-[UIWebSelectTableViewController _selectionNode];
-[UIWebSelectTableViewController _setupGroupsAndOptions];
-[UIWebSelectTableViewController initWithDOMHTMLSelectNode:cachedItems:singleSelectionIndex:multipleSelection:];
-[UIWebSelectTableViewController set_cachedItems:];
-[UIWebSelectTableViewController set_groupsAndOptions:];
-[UIWebSelectTableViewController set_popover:];
-[UIWebSelectTableViewController set_selectionNode:];
```
