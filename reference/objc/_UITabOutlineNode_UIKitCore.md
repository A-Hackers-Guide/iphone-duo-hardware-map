# `_UITabOutlineNode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isGroup;
B _isDestination;
@"NSString" _identifier;
@"NSMutableArray" _children;
@"NSMutableArray" _actions;
@"_UITabOutlineNode" _parent;
```

## Properties

```
@property (T@"_UITabOutlineNode",W,N,V_parent) parent;
@property (TB,N,V_isGroup) isGroup;
@property (TB,N,V_isDestination) isDestination;
@property (T@"NSMutableArray",&,N,V_children) children;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSMutableArray",R,N,V_actions) actions;
```

## Instance methods

```
-[_UITabOutlineNode setChildren:];
-[_UITabOutlineNode identifier];
-[_UITabOutlineNode setParent:];
-[_UITabOutlineNode actions];
-[_UITabOutlineNode parent];
-[_UITabOutlineNode children];
-[_UITabOutlineNode description];
-[_UITabOutlineNode isGroup];
-[_UITabOutlineNode addChild:];
-[_UITabOutlineNode isEqual:];
-[_UITabOutlineNode setIsGroup:];
-[_UITabOutlineNode initWithIdentifier:];
-[_UITabOutlineNode removeChild:];
-[_UITabOutlineNode _descriptionWithIndentationLevel:];
-[_UITabOutlineNode addActionIdentifier:];
-[_UITabOutlineNode isDestination];
-[_UITabOutlineNode setIsDestination:];
```
