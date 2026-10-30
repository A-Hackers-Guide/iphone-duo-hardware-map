# `_UIDebugLogReport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
Q _currentIndentLevel;
@? _fallbackMessagePrefixHandler;
@"NSMutableArray" _statements;
@"NSMutableArray" _prefixStack;
```

## Properties

```
@property (T@"NSMutableArray",&,N,G_statements,V_statements) statements;
@property (T@"NSMutableArray",&,N,G_prefixStack,V_prefixStack) prefixStack;
@property (TQ,R,N) messageCount;
@property (TQ,N,V_currentIndentLevel) currentIndentLevel;
@property (T@?,C,N,V_fallbackMessagePrefixHandler) fallbackMessagePrefixHandler;
```

## Instance methods

```
-[_UIDebugLogReport init];
-[_UIDebugLogReport messageCount];
-[_UIDebugLogReport addMessage:];
-[_UIDebugLogReport setPrefixStack:];
-[_UIDebugLogReport _messagePrefixAtIndentLevel:];
-[_UIDebugLogReport _prefixStack];
-[_UIDebugLogReport _statements];
-[_UIDebugLogReport addLineBreak];
-[_UIDebugLogReport addMessageWithFormat:];
-[_UIDebugLogReport clearAllMessagePrefixes];
-[_UIDebugLogReport currentIndentLevel];
-[_UIDebugLogReport decrementIndentLevel];
-[_UIDebugLogReport decrementIndentLevelAndPopMessagePrefix];
-[_UIDebugLogReport fallbackMessagePrefixHandler];
-[_UIDebugLogReport incrementIndentLevel];
-[_UIDebugLogReport incrementIndentLevelAndPushMessagePrefix:];
-[_UIDebugLogReport popMessagePrefix];
-[_UIDebugLogReport pushMessagePrefix:];
-[_UIDebugLogReport pushMessagePrefixHandler:];
-[_UIDebugLogReport resetIndentLevel];
-[_UIDebugLogReport setCurrentIndentLevel:];
-[_UIDebugLogReport setFallbackMessagePrefixHandler:];
-[_UIDebugLogReport setStatements:];
```
