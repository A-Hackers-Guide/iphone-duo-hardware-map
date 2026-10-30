# `PKPaletteAttributeViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PKPaletteEdgeLocating`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _didExperienceUserInteraction;
B _didSendDismissStatistics;
Q _edgeLocation;
Q _cornerLocation;
@"NSString" _toolIdentifier;
```

## Properties

```
@property (TB,N,V_didSendDismissStatistics) didSendDismissStatistics;
@property (TB,N,V_didExperienceUserInteraction) didExperienceUserInteraction;
@property (T@"NSString",&,N,V_toolIdentifier) toolIdentifier;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteAttributeViewController viewWillAppear:];
-[PKPaletteAttributeViewController viewDidDisappear:];
-[PKPaletteAttributeViewController preferredContentSize];
-[PKPaletteAttributeViewController toolIdentifier];
-[PKPaletteAttributeViewController setToolIdentifier:];
-[PKPaletteAttributeViewController cornerLocation];
-[PKPaletteAttributeViewController didExperienceUserInteraction];
-[PKPaletteAttributeViewController didSendDismissStatistics];
-[PKPaletteAttributeViewController edgeLocation];
-[PKPaletteAttributeViewController setCornerLocation:];
-[PKPaletteAttributeViewController setDidExperienceUserInteraction:];
-[PKPaletteAttributeViewController setDidSendDismissStatistics:];
-[PKPaletteAttributeViewController setEdgeLocation:];
```
