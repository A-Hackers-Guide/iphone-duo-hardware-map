# `CACentralTableViewCell`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 9 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _deviceNameLabel;
@"UILabel" _connectionStatusLabel;
@"UILabel" _inputLabel;
@"UILabel" _slashLabel;
@"UILabel" _outputLabel;
@"UIActivityIndicatorView" _activityIndicator;
@"NSArray" _labelConstraints;
@"NSArray" _activityHConstraints;
@"NSArray" _activityVConstraints;
```

## Properties

```
@property (T@"UILabel",&,N,V_deviceNameLabel) deviceNameLabel;
@property (T@"UILabel",&,N,V_connectionStatusLabel) connectionStatusLabel;
@property (T@"UILabel",&,N,V_inputLabel) inputLabel;
@property (T@"UILabel",&,N,V_slashLabel) slashLabel;
@property (T@"UILabel",&,N,V_outputLabel) outputLabel;
@property (T@"UIActivityIndicatorView",&,N,V_activityIndicator) activityIndicator;
@property (T@"NSArray",&,N,V_labelConstraints) labelConstraints;
@property (T@"NSArray",&,N,V_activityHConstraints) activityHConstraints;
@property (T@"NSArray",&,N,V_activityVConstraints) activityVConstraints;
```

## Instance methods

```
-[CACentralTableViewCell activityIndicator];
-[CACentralTableViewCell dealloc];
-[CACentralTableViewCell updateConstraints];
-[CACentralTableViewCell initWithStyle:reuseIdentifier:];
-[CACentralTableViewCell inputLabel];
-[CACentralTableViewCell setActivityIndicator:];
-[CACentralTableViewCell setInputLabel:];
-[CACentralTableViewCell labelConstraints];
-[CACentralTableViewCell setLabelConstraints:];
-[CACentralTableViewCell deviceNameLabel];
-[CACentralTableViewCell setOutputLabel:];
-[CACentralTableViewCell activityHConstraints];
-[CACentralTableViewCell activityVConstraints];
-[CACentralTableViewCell connectionStatusLabel];
-[CACentralTableViewCell createInitialConstraints];
-[CACentralTableViewCell outputLabel];
-[CACentralTableViewCell setActivityHConstraints:];
-[CACentralTableViewCell setActivityVConstraints:];
-[CACentralTableViewCell setConnectionStatusLabel:];
-[CACentralTableViewCell setDeviceNameLabel:];
-[CACentralTableViewCell setSlashLabel:];
-[CACentralTableViewCell slashLabel];
-[CACentralTableViewCell startIndicator];
-[CACentralTableViewCell stopIndicator];
```
