# url-abridge
Open source, white label URL shortner

# SETUP

1.__Clone the repository locally__ by navigating to your local location and cloning using the link prvoided above. Use the code below:

```
  $ cd [desired_local_location_of_repo]
  $ git clone [https://github.com/jontycg/url-abridge.git]
```

2. Once the repository has been successfully cloned, navigate into the /url-abridge directory and run the following code to __set up
your environment requirements__.  During the execution of this you should be prompted to make a super user (password cannot be too common):

```
  $ bash setup.sh
```

All listed dependencies and requirements should be installed successfully


3. Navigate into /url-abridge and run the following code to __start the virtual environment__ and __run the server__:

```
  $ source venv/bin/activate
  $ cd urlabridge
  $ python manage.py runserver
```

The Virtual Environment should now be running and the __server should have started successfully__

![Server Start](https://lh3.googleusercontent.com/KYbazLNOaSLorGCGun5uwk6NRzTqi0tXfs0B7eut9geRSqNiE_6b_4XNpwp7zsuH7GIMsz9KkWdOJIIWOHSPX-RNxWpmhvIxA9tPu24OfKwuZwrY0MKB-FfWaYDqlm4oVDVAXx50wyTyAyfeDsnG_APuGI-q9nYnd6PrBrWOwA25o3e-Yzv-HZbHzKYv-ar2YDXlxq6SPPsbWEAFBp2-F3bUiDzIATD4uBrTWSM8XfSn8Vwjorxq53oxnQ_e1wxmTPZyxnJn44bhj-HmX7HFgaXOr9CcYMXjPnJJdOnhBhd3fTtJ242uRKMi8Oe9FMLZlw1zoJdmb8IjbONf-vZRPHv_my_lQSVXxgL0JC255lg_ZawyXaZtS4MBZl5OZJ5TtTbtdTDRJ8Hj9zqrTt14HxuwzV2ZFOHDhS_mauEecfhnQyyPhE0Xzs_6Z8HjxzcKFZ6z28ORFd4-zXDQVazrQfQU4hNqul1wB7lZFKg5fG5JFtB6fKxu9NUKByY150Um_yeuFelml3OJkmegcVy4kvzC0gADYbHIMn0Qu0CrI21ISjsJYyG4llRV3fuDiT7sAS9dzet8Fp7QYvUjQZ5IDo4luIV_CsFHSKk3l-sYv-Wln8ugs8GcLCJXiN1B8oPVhwZ2WegjKcSqbB7wM8g-mrcmCEYjqz_W4G2v1sI9nehLb5UvYj2gqg=w958-h358-no)

7. In your internet browser navigate to __http://localhost:8000/admin/__ and login using the credentials you created during super user creation:

![Admin Login](https://lh3.googleusercontent.com/isFdhPkGGwwtgz_QfNR7DXbxDIbBU8FMEqkBBEv3KM0Rqml9EiCcIxW0flMR3_jYelglnYe-qJ16UoQE0g1ciBQgCmXDXDe7P82yYRzgGInQMiixz4sf8gmlJXq66WlBJzisELk1MkMFidDMqRQuIGE37Q8kMeWFvR_3kuyH7twHtxWlmtlLAVIi4-R75O22Q4vqFbC1oLkkFBZOI_oiduGQ3ufX_kChN_G6gAeJvE88LWC60oP9SUhhXnRQ2mUS9mlmmLh36lg5Q7V3ptGkV-qDJL3ytygesKtn9kicz3PD90Lyst54ZrzN6IBCrk97EeqSpqZlhG7Qfa_pJnxtotFkBqBiBeHdmOQMksjIbYTDLt94_gCcpPL695AGxZ6EI78DEI-hembZZfQwm-N48qztiwLTSq0JkoPbh3N_JCHvnS4LARW_wYI8lXbZC9E-RXLxg_LsKD6m2nJKxpOZ15tD5tojCYR9vTr3B-kRW78vdfDwDSZb8PP_svQlq-4k3bJeWcQwrh_nK3vIMUOnlZN-s3_EyckXXowW1X67oZMhw7zmwp6JrFmIgkOHfzNNoV5BIZFfGvdU3ldx9hgDEGUch2blgAjIDEZLXFOVg8vKjWNHmDEWRzxmRnDR5Y_tjTHFlsHIEYjOW4yqO2HqO378xPtAMqcksxhtsBIVs6_gNPpNxpUkiw=w796-h596-no)

8. Once Authenticated you should have access to the __Django Admin Panel__:

![Admin Panel](https://lh3.googleusercontent.com/nAOfLLWcBfhLr2r1YaEuFjPvloFhh07YV358kKNawTSMqgolui6uMDIgtt_DMLyRKwpRiyJ_vOIxvO-g85Yl1jejQluZYHtWiPO7BvkZpfnXruz5MYCMmqztZca6xuM3hVnkmwY-F8Xtf4rGHJSUdz8wJP2UHGt7uCvihPsR0nSN4kCodRs25rWtOAyb_QBeoYQX92j1PRN8w4iOSSjDJlTExMd0LsbRo_DkH8Y-lqiGyraiLdCL8eL_l4yhovwgK_J5TP5o-8pOwcJSAEXourG19bzyPHGeCT19OwhRTI6GcwezY2G4wa0y1crtCjpEX2dKmY3PULoDCPm3Vq7RigclpcvNxG5HnJK0i0Rsf7nio1h7eSF6GOevL6IqdLqgZPXs7faqLxnNw9WeBNk19iC3_2wFkCsz_vgYD2FRhrj7OAGYrJYYpxanf_1nT51dZZLuPrhRg3eVwBYVVzDmoUr1VCbLGjI2D7NguIz5Q5Ga5U0JCeo7OmH1KB5O0rDX042V0Xa_loW2T2zg4uhehER6O0bdaQX4dadv22mUWssqZIBngOMsNEm82JU2YdjEovGUtbQY9yWPv5arpZiBPYBqTmDm_GMw5lh2bp22A1cFQrDxwZw_Z_AI7A1mlCwEPkKMwqKOfjOGnvgU_PBYY0E4pEpzHY4vuy1RcoMoo0iC0rnTTv4oag=w954-h362-no)

9. __Quit the server__ with CONTROL-C 

10. Quit the virtual environment by running the following code in the terminal:

```
  $ deactivate
```

## SETTING ENVIRONMENT VARIABLES

__NOTE:__When deploying to prod make sure you set the When deploying to prod make sure you set the URLABRIDGE_SECRET_KEY and URLABRIDGE_DEBUG environment variables. and URLABRIDGE_DEBUG environment variables.

URLABRIDGE_SECRET_KEY = [Your Secret Key]
URLABRIDGE_DEBUG = [True or False]
