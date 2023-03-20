import os
import yaml
import argparse
import streamlit_authenticator as stauth

def define_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--userid",
            type=str,
            required=True)
    parser.add_argument(
            "--name",
            type=str,
            required=True)
    parser.add_argument(
            "--password",
            type=str,
            required=True)
    parser.add_argument(
            "--email",
            type=str,
            required=True)

    args = parser.parse_args()

    return args

def get_yaml_form(args):
    '''
    Args :
        args : argparse.ArgumentParser
    Returns :
        yaml format data of user credentail
    '''
    data = {
        "credentials" : {
            "usernames" : {
                args.userid : {
                    "name" : args.name,
                    "password" :stauth.Hasher([args.password]).generate()[0] 
                    },
                }
        },
        "cookie": {
            "expiry_days" : 0, # 만료일, 재인증 기능 필요없으면 0으로 세팅
            "key": "some_signature_key",
            "name" : "some_cookie_name"
        },
        "preauthorized" : {
            "emails" : [
                args.email
            ]
        }
    }

    return data

def dump_yaml(data, save_pth="./", save_fn="config.yaml"):
    '''
    Args :
        data : yaml format data of user credential
    '''
    with open(os.path.join(save_pth, save_fn),'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    
if __name__ == '__main__':
    args = define_argparser()
    data = get_yaml_form(args)
    dump_yaml(data, save_pth="./", save_fn="config.yaml")
