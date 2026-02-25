"""
MNE Sample Data
"""
study_name = 'ds000248'
bids_root = f'/Users/vyompaknikar/Desktop/EEG Dataset/ANALYSE_248/{study_name}'
deriv_root = f'{bids_root}/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

subjects = ['01']
rename_events = {'Smiley': 'Emoji', 'Button': 'Switch'}
conditions = ['Auditory', 'Visual', 'Auditory/Left', 'Auditory/Right']
contrasts = [('Visual', 'Auditory'), ('Auditory/Right', 'Auditory/Left')]

time_frequency_conditions = ['Auditory', 'Visual']

ch_types = ['meg']
mf_reference_run = '01'
find_flat_channels_meg = True
find_noisy_channels_meg = True
use_maxwell_filter = True

epochs_tmin = -0.2
epochs_tmax = 0.5
baseline = (None, 0)
noise_cov = (None, 0)

spatial_filter = 'ssp'
n_proj_eog = dict(n_mag=1, n_grad=1, n_eeg=1)
n_proj_ecg = dict(n_mag=1, n_grad=1, n_eeg=0)
ssp_meg = "combined"
ecg_proj_from_average = True
eog_proj_from_average = False
epochs_decim = 4

bem_mri_images = "FLASH"
recreate_bem = False

n_jobs = 1

# bem_mri_images = 'FLASH'
# recreate_bem = True
# recreate_scalp_surface = True

# report_evoked_n_time_points = 3
# report_stc_n_time_points = 3


# def mri_t1_path_generator(bids_path):
#     # don't really do any modifications – just for testing!
#     return bids_path

# process_er = False
# def noise_cov(bp):
#     # Use pre-stimulus period as noise source
#     bp = bp.copy().update(processing='clean', suffix='epo')
#     epo = mne.read_epochs(bp)
#     cov = mne.compute_covariance(epo, rank='info', tmax=0)
#     return cov

# epochs_metadata_query = 'index > 0'  # Just for testing!

on_error = "debug"

# import mne

# mne_bids_pipeline --config config_ds000248.py

