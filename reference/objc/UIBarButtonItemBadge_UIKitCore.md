# `UIBarButtonItemBadge`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `NSCoding`
- 1 instance variables, 5 properties, 13 instance methods, 4 class methods

## Instance variables

```
backingBadge;
```

## Properties

```
@property (T@"NSString",N,R) stringValue;
@property (T@"UIColor",N,&) foregroundColor;
@property (T@"UIColor",N,&) backgroundColor;
@property (T@"UIFont",N,&) font;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UIBarButtonItemBadge supportsSecureCoding];
+[UIBarButtonItemBadge badgeWithCount:];
+[UIBarButtonItemBadge badgeWithString:];
+[UIBarButtonItemBadge indicatorBadge];
```

## Instance methods

```
-[UIBarButtonItemBadge setForegroundColor:];
-[UIBarButtonItemBadge stringValue];
-[UIBarButtonItemBadge init];
-[UIBarButtonItemBadge setBackgroundColor:];
-[UIBarButtonItemBadge encodeWithCoder:];
-[UIBarButtonItemBadge backgroundColor];
-[UIBarButtonItemBadge description];
-[UIBarButtonItemBadge initWithCoder:];
-[UIBarButtonItemBadge font];
-[UIBarButtonItemBadge foregroundColor];
-[UIBarButtonItemBadge copyWithZone:];
-[UIBarButtonItemBadge isEqual:];
-[UIBarButtonItemBadge setFont:];
```
