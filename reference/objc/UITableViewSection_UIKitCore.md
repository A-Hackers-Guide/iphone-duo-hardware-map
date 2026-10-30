# `UITableViewSection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _headerTitle;
@"UIView" _headerView;
@"NSString" _footerTitle;
@"UIView" _footerView;
@"NSArray" _rows;
```

## Properties

```
@property (T@"NSString",C,N,V_headerTitle) headerTitle;
@property (T@"UIView",&,N,V_headerView) headerView;
@property (T@"NSString",C,N,V_footerTitle) footerTitle;
@property (T@"UIView",&,N,V_footerView) footerView;
@property (T@"NSArray",C,N,V_rows) rows;
```

## Class methods

```
+[UITableViewSection sectionWithRows:];
```

## Instance methods

```
-[UITableViewSection setFooterView:];
-[UITableViewSection rows];
-[UITableViewSection headerView];
-[UITableViewSection footerView];
-[UITableViewSection setHeaderTitle:];
-[UITableViewSection encodeWithCoder:];
-[UITableViewSection initWithCoder:];
-[UITableViewSection setRows:];
-[UITableViewSection setHeaderView:];
-[UITableViewSection headerTitle];
-[UITableViewSection setFooterTitle:];
-[UITableViewSection footerTitle];
```
