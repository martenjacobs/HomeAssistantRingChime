# HomeAssistantRingChime
Notify component to enable messages to Ring Chime in Home Assistant 

## Usage
- Place the python file in this repo in your custom_components folder
- Set up your Ring-account in your [Home Assistant config](https://www.home-assistant.io/components/ring/)
- Set up this component:
```yaml
notify:
  platform: ring
```
- Restart Home Assistant
- Your chimes will now show up as notify-services
